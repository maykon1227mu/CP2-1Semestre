# ENTRADA
cp1 = float(input())
cp2 = float(input())
cp3 = float(input())
sp1 = float(input())
sp2 = float(input())
gs = float(input())

# LÓGICA
if cp1 <= cp2 and cp1 <= cp3:
    menor = cp1
elif cp2<= cp1 and cp2 <= cp3:
    menor = cp2
else:
    menor = cp3

media = (((cp1 + cp2 + cp3 - menor + sp1 + sp2) / 4) * 0.4) + (gs * 0.6)
mediaPeso = media * 0.4

# SAÍDA
print(f"Média do semestre: {media:.1f}")
print(f"Média do semestre com peso: {mediaPeso:.1f}")
