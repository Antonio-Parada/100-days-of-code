; bootloader.asm
; A very simple bootloader that loads the kernel

[org 0x7c00]

; Set up segment registers
mov ax, 0x07C0
mov ds, ax
mov es, ax
mov fs, ax
mov gs, ax
mov ss, ax
mov sp, 0x7c00

; Print a message
mov si, msg
call print_string

; Load kernel (conceptual - in a real scenario, this would involve disk I/O)
; For this example, we assume the kernel is already loaded at 0x1000
mov ax, 0x1000
call ax

; Infinite loop
jmp $

; Data
msg db "Booting simple OS...", 0

; Print string function
print_string:
    lodsb
    cmp al, 0
    je done
    mov ah, 0x0e
    int 0x10
    jmp print_string
done:
    ret

; Boot sector padding
times 510 - ($ - $$) db 0
dw 0xaa55
