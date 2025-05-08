// dllmain.cpp
#include <windows.h>

BOOL APIENTRY DllMain(HMODULE hModule,
                      DWORD  ul_reason_for_call,
                      LPVOID lpReserved)
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        // DLL被加载时执行的代码
        MessageBox(NULL, L"DLL Injected into svchost!", L"Success", MB_OK);
        break;
    case DLL_PROCESS_DETACH:
        // DLL被卸载时执行的代码
        break;
    }
    return TRUE;
}