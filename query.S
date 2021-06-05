





00000000 <query_func>:
  4087ed:	c9                   	leave  
  4087ee:	c2 24 00             	ret    0x24
  4087f1:	55                   	push   ebp
  4087f2:	8b ec                	mov    ebp,esp
  4087f4:	51                   	push   ecx
  4087f5:	56                   	push   esi
  4087f6:	8b f1                	mov    esi,ecx
  4087f8:	81 7e 08 01 00 01 80 	cmp    DWORD PTR [esi+0x8],0x80010001
  4087ff:	74 70                	je     0x408871
  408801:	8b 06                	mov    eax,DWORD PTR [esi]
  408803:	85 c0                	test   eax,eax
  408805:	74 6a                	je     0x408871
  408807:	8b 40 4c             	mov    eax,DWORD PTR [eax+0x4c]
  40880a:	8b 08                	mov    ecx,DWORD PTR [eax]
  40880c:	8d 55 fc             	lea    edx,[ebp-0x4]
  40880f:	52                   	push   edx
  408810:	68 28 d3 42 00       	push   0x42d328
  408815:	50                   	push   eax
  408816:	ff 11                	call   DWORD PTR [ecx]
  408818:	85 c0                	test   eax,eax
  40881a:	7c 24                	jl     0x408840
  40881c:	8b 45 fc             	mov    eax,DWORD PTR [ebp-0x4]
  40881f:	8b 08                	mov    ecx,DWORD PTR [eax]
  408821:	8d 56 10             	lea    edx,[esi+0x10]
  408824:	52                   	push   edx
  408825:	33 d2                	xor    edx,edx
  408827:	39 56 0c             	cmp    DWORD PTR [esi+0xc],edx
  40882a:	0f 95 c2             	setne  dl
  40882d:	52                   	push   edx
  40882e:	ff 76 08             	push   DWORD PTR [esi+0x8]
  408831:	50                   	push   eax
  408832:	ff 51 0c             	call   DWORD PTR [ecx+0xc]
  408835:	8b 45 fc             	mov    eax,DWORD PTR [ebp-0x4]
  408838:	8b 08                	mov    ecx,DWORD PTR [eax]
  40883a:	50                   	push   eax
  40883b:	ff 51 08             	call   DWORD PTR [ecx+0x8]
  40883e:	eb 31                	jmp    0x408871
  408840:	8b ce                	mov    ecx,esi
  408842:	e8 a4 ef ff ff       	call   0x4077eb
  408847:	85 c0                	test   eax,eax
  408849:	74 26                	je     0x408871
  40884b:	8b 4e 0c             	mov    ecx,DWORD PTR [esi+0xc]
  40884e:	83 b9 8c 00 00 00 00 	cmp    DWORD PTR [ecx+0x8c],0x0
  408855:	6a 0d                	push   0xd
  408857:	5a                   	pop    edx
  408858:	74 05                	je     0x40885f
  40885a:	ba 0d 80 00 00       	mov    edx,0x800d
  40885f:	8b 0e                	mov    ecx,DWORD PTR [esi]
  408861:	57                   	push   edi
  408862:	8b 39                	mov    edi,DWORD PTR [ecx]
  408864:	50                   	push   eax
  408865:	52                   	push   edx
  408866:	ff 76 08             	push   DWORD PTR [esi+0x8]
  408869:	51                   	push   ecx
  40886a:	ff 57 70             	call   DWORD PTR [edi+0x70]
  40886d:	83 c4 10             	add    esp,0x10
  408870:	5f                   	pop    edi
  408871:	5e                   	pop    esi
  408872:	c9                   	leave  
  408873:	c3                   	ret    