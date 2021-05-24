LCFI242:
	mov	ebp, esp
LCFI243:
	sub	esp, 4
	mov	DWORD PTR [ebp-4], ecx
	mov	eax, DWORD PTR [ebp-4]
	mov	edx, DWORD PTR [eax+4]
	mov	eax, DWORD PTR [ebp-4]
	mov	eax, DWORD PTR [eax]
	sub	edx, eax
	mov	eax, edx
	sar	eax, 3
	leave
LCFI244:
	ret
LFE8475:
	.section	.text$_ZNSt16allocator_traitsISaISt4pairIiiEEE8allocateERS2_j,"x"
	.linkonce discard
	.globl	__ZNSt16allocator_traitsISaISt4pairIiiEEE8allocateERS2_j
	.def	__ZNSt16allocator_traitsISaISt4pairIiiEEE8allocateERS2_j;	.scl	2;	.type	32;	.endef
__ZNSt16allocator_traitsISaISt4pairIiiEEE8allocateERS2_j:
LFB8476:
	push	ebp
LCFI245:
	mov	ebp, esp
LCFI246:
	sub	esp, 24
	mov	DWORD PTR [esp+4], 0
	mov	eax, DWORD PTR [ebp+12]
	mov	DWORD PTR [esp], eax
	mov	ecx, DWORD PTR [ebp+8]
	call	__ZN9__gnu_cxx13new_allocatorISt4pairIiiEE8allocateEjPKv
	sub	esp, 8
	leave
LCFI247:
	ret
LFE8476:
	.section	.text$_ZSt32__make_move_if_noexcept_iteratorISt4pairIiiESt13move_iteratorIPS1_EET0_PT_,"x"
	.linkonce discard
	.globl	__ZSt32__make_move_if_noexcept_iteratorISt4pairIiiESt13move_iteratorIPS1_EET0_PT_
	.def	__ZSt32__make_move_if_noexcept_iteratorISt4pairIiiESt13move_iteratorIPS1_EET0_PT_;	.scl	2;	.type	32;	.endef
__ZSt32__make_move_if_noexcept_iteratorISt4pairIiiESt13move_iteratorIPS1_EET0_PT_:
LFB8477:
	push	ebp
LCFI248:
	mov	ebp, esp
LCFI249:
	sub	esp, 40
	lea	eax, [ebp-12]
	mov	edx, DWORD PTR [ebp+8]
	mov	DWORD PTR [esp], edx
	mov	ecx, eax
	call	__ZNSt13move_iteratorIPSt4pairIiiEEC1ES2_
	sub	esp, 4
	mov	eax, DWORD PTR [ebp-12]
	leave
LCFI250:
	ret
LFE8477:
	.section	.text$_ZSt22__uninitialized_copy_aISt13move_iteratorIPSt4pairIiiEES3_S2_ET0_T_S6_S5_RSaIT1_E,"x"
	.linkonce discard
	.globl	__ZSt22__uninitialized_copy_aISt13move_iteratorIPSt4pairIiiEES3_S2_ET0_T_S6_S5_RSaIT1_E
	.def	__ZSt22__uninitialized_copy_aISt13move_iteratorIPSt4pairIiiEES3_S2_ET0_T_S6_S5_RSaIT1_E;	.scl	2;	.type	32;	.endef
__ZSt22__uninitialized_copy_aISt13move_iteratorIPSt4pairIiiEES3_S2_ET0_T_S6_S5_RSaIT1_E:
LFB8478:
	push	ebp
LCFI251:
	mov	ebp, esp
LCFI252:
	sub	esp, 24
	mov	eax, DWORD PTR [ebp+16]
	mov	DWORD PTR [esp+8], eax
	mov	eax, DWORD PTR [ebp+12]
	mov	DWORD PTR [esp+4], eax
	mov	eax, DWORD PTR [ebp+8]
	mov	DWORD PTR [esp], eax
	call	__ZSt18uninitialized_copyISt13move_iteratorIPSt4pairIiiEES3_ET0_T_S6_S5_
	leave
LCFI253:
	ret
LFE8478:
	.section	.text$_ZN9__gnu_cxx13new_allocatorISt4pairIiiEE7destroyIS2_EEvPT_,"x"
	.linkonce discard
	.align 2
	.globl	__ZN9__gnu_cxx13new_allocatorISt4pairIiiEE7destroyIS2_EEvPT_
	.def	__ZN9__gnu_cxx13new_allocatorISt4pairIiiEE7destroyIS2_EEvPT_;	.scl	2;	.type	32;	.endef
__ZN9__gnu_cxx13new_allocatorISt4pairIiiEE7destroyIS2_EEvPT_:
LFB8479:
	push	ebp
LCFI254:
	mov	ebp, esp
LCFI255:
	sub	esp, 4
	mov	DWORD PTR [ebp-4], ecx
	nop
	leave
LCFI256:
	ret	4
LFE8479:
	.section	.text$_ZSt8_DestroyIPSt4pairIiiEEvT_S3_,"x"
	.linkonce discard
	.globl	__ZSt8_DestroyIPSt4pairIiiEEvT_S3_
	.def	__ZSt8_DestroyIPSt4pairIiiEEvT_S3_;	.scl	2;	.type	32;	.endef
__ZSt8_DestroyIPSt4pairIiiEEvT_S3_:
LFB8480:
	push	ebp
LCFI257:
	mov	ebp, esp
LCFI258:
	sub	esp, 24
	mov	eax, DWORD PTR [ebp+12]
	mov	DWORD PTR [esp+4], eax
	mov	eax, DWORD PTR [ebp+8]
	mov	DWORD PTR [esp], eax
	call	__ZNSt12_Destroy_auxILb1EE9__destroyIPSt4pairIiiEEEvT_S5_
	nop
	leave
LCFI259:
	ret
LFE8480: