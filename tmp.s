	.file	"a.c"
	.intel_syntax noprefix
	.text
	.section .rdata,"dr"
LC0:
	.ascii "hi\0"
	.text
	.globl	__Z3relv
	.def	__Z3relv;	.scl	2;	.type	32;	.endef
__Z3relv:
LFB15:
	push	ebp
LCFI0:
	mov	ebp, esp
LCFI1:
	sub	esp, 24
	mov	DWORD PTR [esp], OFFSET FLAT:LC0
	call	_printf
	mov	eax, 2
	leave
LCFI2:
	ret
LFE15:
	.def	___main;	.scl	2;	.type	32;	.endef
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB16:
	push	ebp
LCFI3:
	mov	ebp, esp
LCFI4:
	and	esp, -16
	sub	esp, 16
	call	___main
	mov	DWORD PTR [esp+12], 0
	mov	DWORD PTR [esp+8], 0
	mov	edx, DWORD PTR [esp+8]
	mov	eax, DWORD PTR [esp+12]
	add	eax, edx
	mov	DWORD PTR [esp+4], eax
	call	__Z3relv
	mov	eax, 0
	leave
LCFI5:
	ret
LFE16:
	.ident	"GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
	.def	_printf;	.scl	2;	.type	32;	.endef
