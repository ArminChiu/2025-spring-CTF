undefined8 main(void) {
  undefined local_28 [32];
  
  setvbuf(stdin,(char *)0x0,2,0);
  setvbuf(stdout,(char *)0x0,2,0);
  puts("input:");
  read(0,local_28,0x100);
  return 0;
}

void backdoor(void) {
  system("/bin/sh");
  return;
}



