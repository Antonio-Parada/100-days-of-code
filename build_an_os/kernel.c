// kernel.c

void main()
{
    char *video_memory = (char *)0xb8000;
    *video_memory = 'H';
    *(video_memory + 1) = 0x0f; // White on black
    *(video_memory + 2) = 'e';
    *(video_memory + 3) = 0x0f;
    *(video_memory + 4) = 'l';
    *(video_memory + 5) = 0x0f;
    *(video_memory + 6) = 'l';
    *(video_memory + 7) = 0x0f;
    *(video_memory + 8) = 'o';
    *(video_memory + 9) = 0x0f;
    *(video_memory + 10) = ',';
    *(video_memory + 11) = 0x0f;
    *(video_memory + 12) = ' ';
    *(video_memory + 13) = 0x0f;
    *(video_memory + 14) = 'O';
    *(video_memory + 15) = 0x0f;
    *(video_memory + 16) = 'S';
    *(video_memory + 17) = 0x0f;

    while(1);
}