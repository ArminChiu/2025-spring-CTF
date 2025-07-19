
undefined8 main(void) {
  int iVar1;
  long in_FS_OFFSET;
  int local_7c;
  undefined local_78 [104];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  puts(&DAT_001020c0);
  puts(&DAT_001020e8);
  do {
    puts(&DAT_0010210f);
    puts(&DAT_00102123);
    puts(&DAT_00102133);
    printf(&DAT_0010213d);
    __isoc99_scanf(&DAT_00102149,&local_7c);
    if (local_7c == 3) {
      puts(&DAT_001021bf);
LAB_00101468:
      if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
        return 0;
      }
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    if (local_7c < 4) {
      if (local_7c == 1) {
        printf(&DAT_0010214c);
        __isoc99_scanf(&DAT_0010215c,local_78);
        iVar1 = check_flag(local_78);
        if (iVar1 != 0) {
          puts(&DAT_0010215f);
          puts(&DAT_00102178);
          goto LAB_00101468;
        }
        puts(&DAT_001021a0);
      }
      else {
        if (local_7c != 2) goto LAB_0010144a;
        show_hint();
      }
    }
    else {
LAB_0010144a:
      puts(&DAT_001021c9);
    }
    putchar(10);
  } while( true );
}

undefined8 check_flag(char *param_1) {
  size_t sVar1;
  undefined8 uVar2;
  int local_10;
  
  sVar1 = strlen(param_1);
  if ((int)sVar1 == 0x11) {
    for (local_10 = 0; local_10 < 0x11; local_10 = local_10 + 1) {
      if ((int)(char)(param_1[local_10] ^ 0x42) != (uint)(byte)encrypted_flag[local_10]) {
        return 0;
      }
    }
    uVar2 = 1;
  }
  else {
    uVar2 = 0;
  }
  return uVar2;
}


void decrypt_flag(void) {
  int local_c;
  
  printf(&DAT_001020a8);
  for (local_c = 0; local_c < 0x11; local_c = local_c + 1) {
    putchar((uint)(encrypted_flag[local_c] ^ 0x42));
  }
  putchar(10);
  return;
}

