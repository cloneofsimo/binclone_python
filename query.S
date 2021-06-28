





00000000 <query_func>:
L285:
	lea	eax, [ebp+20]
	mov	DWORD PTR [esp], eax
	call	__ZSt4moveIRSt4pairIiiEEONSt16remove_referenceIT_E4typeEOS4_
	mov	ebx, eax
	mov	eax, DWORD PTR [ebp+12]
	mov	DWORD PTR [esp], eax
	lea	ecx, [ebp+8]
	call	__ZNK9__gnu_cxx17__normal_iteratorIPSt4pairIiiESt6vectorIS2_SaIS2_EEEplEi
	sub	esp, 4
	mov	DWORD PTR [ebp-16], eax
	lea	eax, [ebp-16]
	mov	ecx, eax
	call	__ZNK9__gnu_cxx17__normal_iteratorIPSt4pairIiiESt6vectorIS2_SaIS2_EEEdeEv
	mov	DWORD PTR [esp], ebx
	mov	ecx, eax
	call	__ZNSt4pairIiiEaSEOS0_
	sub	esp, 4
	nop
	mov	ebx, DWORD PTR [ebp-4]
	leave
LCFI395:
	ret
LFE8554:
	.section	.text$_ZNSt4pairIiiE4swapERS0_,"x"
	.linkonce discard
	.align 2
	.globl	__ZNSt4pairIiiE4swapERS0_
	.def	__ZNSt4pairIiiE4swapERS0_;	.scl	2;	.type	32;	.endef
__ZNSt4pairIiiE4swapERS0_:
LFB8555:
	push	ebp
LCFI396:
	mov	ebp, esp
LCFI397:
	sub	esp, 40
	mov	DWORD PTR [ebp-12], ecx
	mov	edx, DWORD PTR [ebp+8]
	mov	eax, DWORD PTR [ebp-12]
	mov	DWORD PTR [esp+4], edx
	mov	DWORD PTR [esp], eax
	call	__ZSt4swapIiENSt9enable_ifIXsrSt6__and_IJSt6__not_ISt15__is_tuple_likeIT_EESt21is_move_constructibleIS4_ESt18is_move_assignableIS4_EEE5valueEvE4typeERS4_SE_
	mov	eax, DWORD PTR [ebp+8]
	lea	edx, [eax+4]
	mov	eax, DWORD PTR [ebp-12]
	add	eax, 4
	mov	DWORD PTR [esp+4], edx
	mov	DWORD PTR [esp], eax
	call	__ZSt4swapIiENSt9enable_ifIXsrSt6__and_IJSt6__not_ISt15__is_tuple_likeIT_EESt21is_move_constructibleIS4_ESt18is_move_assignableIS4_EEE5valueEvE4typeERS4_SE_
	nop
	leave
LCFI398:
	ret	4
LFE8555:
	.section	.text$_ZNSt20__copy_move_backwardILb1ELb0ESt26random_access_iterator_tagE13__copy_move_bIPSt4pairIiiES5_EET0_T_S7_S6_,"x"
	.linkonce discard
	.globl	__ZNSt20__copy_move_backwardILb1ELb0ESt26random_access_iterator_tagE13__copy_move_bIPSt4pairIiiES5_EET0_T_S7_S6_
	.def	__ZNSt20__copy_move_backwardILb1ELb0ESt26random_access_iterator_tagE13__copy_move_bIPSt4pairIiiES5_EET0_T_S7_S6_;	.scl	2;	.type	32;	.endef
__ZNSt20__copy_move_backwardILb1ELb0ESt26random_access_iterator_tagE13__copy_move_bIPSt4pairIiiES5_EET0_T_S7_S6_:
LFB8556: