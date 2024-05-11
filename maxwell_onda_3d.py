import numpy as np
import matplotlib.pyplot as plt

# Constantes físicas
c = 299792458  # Velocidade da luz no vácuo (m/s)
mu0 = 4e-7 * np.pi  # Permeabilidade magnética do vácuo (H/m)
eps0 = 8.854187817e-12  # Permissividade elétrica do vácuo (F/m)

# Parâmetros da simulação
nx = 100  # Número de pontos no eixo x
ny = 100  # Número de pontos no eixo y
nz = 100  # Número de pontos no eixo z
dx = 1e-3  # Resolução espacial (m)
dy = 1e-3  # Resolução espacial (m)
dz = 1e-3  # Resolução espacial (m)
dt = 1e-12  # Passo temporal (s)
nt = 1000  # Número de passos temporais

# Constantes do material
epsr = 4.0  # Permissividade relativa do meio
mur = 1.0  # Permeabilidade relativa do meio

# Criando os grids
x = np.linspace(-nx/2 * dx, nx/2 * dx, nx)
y = np.linspace(-ny/2 * dy, ny/2 * dy, ny)
z = np.linspace(-nz/2 * dz, nz/2 * dz, nz)

# Criando os campos eletromagnéticos
Ex = np.zeros((nx, ny, nz))
Ey = np.zeros((nx, ny, nz))
Ez = np.zeros((nx, ny, nz))
Hx = np.zeros((nx, ny, nz))
Hy = np.zeros((nx, ny, nz))
Hz = np.zeros((nx, ny, nz))

xs = nx // 2
ys = ny // 2
zs = nz // 2

# Simulação FDTD
for n in range(nt):
    # Atualizando campos elétricos
    Ex[1:-1, 1:-1, 1:-1] = (
        Ex[1:-1, 1:-1, 1:-1]
        - c * dt / (epsr * mu0) * (Hy[1:-1, 2:, 1:-1] - Hy[1:-1, :-1, 1:-1])
        - c * dt / (epsr * mu0) * (Hz[2:, 1:-1, 1:-1] - Hz[:-1, 1:-1, 1:-1])
    )
    Ey[1:-1, 1:-1, 1:-1] = (
        Ey[1:-1, 1:-1, 1:-1]
        - c * dt / (epsr * mu0) * (Hx[2:, 1:-1, 1:-1] - Hx[:-1, 1:-1, 1:-1])
        - c * dt / (epsr * mu0) * (Hz[1:-1, 2:, 1:-1] - Hz[1:-1, :-1, 1:-1])
    )
    Ez[1:-1, 1:-1, 1:-1] = (
        Ez[1:-1, 1:-1, 1:-1]
        - c * dt / (epsr * mu0) * (Hx[1:-1, 2:, 1:-1] - Hx[1:-1, :-1, 1:-1])
        - c * dt / (epsr * mu0) * (Hy[1:-1, 1:-1, 2:] - Hy[1:-1, 1:-1, :-1])
    )

    # Atualizando campos magnéticos
    Hx[1:-1, 1:-1, 1:-1] = (
        Hx[1:-1, 1:-1, 1:-1]
        + c
