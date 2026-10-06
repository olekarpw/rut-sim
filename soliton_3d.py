import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Soliton6DVisualizer:
    def __init__(self, psi_p_deg=77.636):
        self.psi_p = np.radians(psi_p_deg)
        self.R = 3.0  # Большой радиус тора (макро-масштаб вакуумного узла)
        self.r = 1.0  # Малый радиус тора (микро-радиус фазовой нити)

    def generate_torus_soliton(self, n, num_points=1000):
        """
        Генерация траектории фазовой намотки солитона для n-го поколения.
        n: число фазовых оборотов (n=1, 2, 3 — устойчивые, n=4 — срыв).
        """
        u = np.linspace(0, 2 * np.pi, num_points)  # Полоидальный угол
        v = n * u + self.psi_p                     # Тороидальный угол с фазовым сдвигом Psi_p

        # Проекция из 6D фазового пространства в 3D
        x = (self.R + self.r * np.cos(v)) * np.cos(u)
        y = (self.R + self.r * np.cos(v)) * np.sin(u)
        z = self.r * np.sin(v) + 0.2 * np.sin(n * v) # Фазовая модуляция субстрата

        return x, y, z

    def plot_solitons(self):
        """Отрисовка 3D-проекций солитонов для n=1,2,3 и запрещенного n=4"""
        fig = plt.figure(figsize=(14, 10))
        fig.suptitle(r'Топология вакуумных солитонов RUT в 6D (Проекция на $R^3$)', fontsize=14, fontweight='bold')

        titles = [
            r'n=1: Электрон ($e^-$) — Стабильный узел',
            r'n=2: Мюон ($\mu^-$) — 2-я гармоника',
            r'n=3: Тау-лептон ($\tau^-$) — Предел устойчивости',
            r'n=4: Запрещенное состояние — Самопересечение'
        ]
        colors = ['mediumblue', 'forestgreen', 'darkorange', 'crimson']

        for i, n in enumerate([1, 2, 3, 4], 1):
            ax = fig.add_subplot(2, 2, i, projection='3d')
            
            # Поверхность опорного тора (пространственный субстрат)
            u_surf = np.linspace(0, 2 * np.pi, 30)
            v_surf = np.linspace(0, 2 * np.pi, 30)
            U, V = np.meshgrid(u_surf, v_surf)
            X_surf = (self.R + self.r * np.cos(V)) * np.cos(U)
            Y_surf = (self.R + self.r * np.cos(V)) * np.sin(U)
            Z_surf = self.r * np.sin(V)
            
            ax.plot_surface(X_surf, Y_surf, Z_surf, color='gray', alpha=0.15, edgecolor='none')

            # Линия фазового солитона
            x, y, z = self.generate_torus_soliton(n)
            
            if n == 4:
                # Визуализация декогеренции и срыва фазы при n=4
                ax.plot(x[:700], y[:700], z[:700], color=colors[i-1], lw=2, label='Фазовая намотка')
                ax.plot(x[700:], y[700:], z[700:], color='black', linestyle=':', lw=2, label='Декогеренция (срыв)')
            else:
                ax.plot(x, y, z, color=colors[i-1], lw=2.5, label=f'Фазовый узел n={n}')

            ax.set_title(titles[i-1], fontsize=11)
            ax.set_axis_off()  # Убираем оси для чистой топологической картинки
            ax.legend(loc='upper right', fontsize=9)

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    viz = Soliton6DVisualizer()
    viz.plot_solitons()
