import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Planet:
    def __init__(self, ime, d, M, v_x, v_y=0):
        self.ime = ime
        self.M = M
        self.d = d
        self.v_x = v_x
        self.v_y = v_y
        self.poz = np.array([0, d], dtype=float)
        self.brzina = np.array([v_x, v_y], dtype=float)
        self.lista_x = []
        self.lista_y = []
        self.evolucija1=0
        self.evolucija2=0

class Svemir:
    def __init__(self, dt, t, lista_planeta=None):
        if lista_planeta is None:
            lista_planeta = []
        self.dt = dt
        self.t = t
        self.G = 6.67408 * (10 ** -11)
        self.lista_planeta = lista_planeta

    def add_planet(self, planet):
        self.lista_planeta.append(planet)

    def trajektorij(self):
        timer = 0
        num_steps = int(self.t / self.dt)
        self.steps_data = [[] for _ in self.lista_planeta]

        # Initial forces
        forces = [self.calculate_net_force(planet) for planet in self.lista_planeta]

        for step in range(num_steps):
            for i, planet in enumerate(self.lista_planeta):
                # Verlet integration
                a = forces[i] / planet.M
                new_poz = planet.poz + planet.brzina * self.dt + 0.5 * a * self.dt**2
                self.steps_data[i].append(new_poz)
                new_forces = self.calculate_net_force(planet, new_poz)
                new_a = new_forces / planet.M
                new_brzina = planet.brzina + 0.5 * (a + new_a) * self.dt
                
                # Update positions and velocities
                planet.poz = new_poz
                planet.brzina = new_brzina
                planet.lista_x.append(planet.poz[0])
                planet.lista_y.append(planet.poz[1])

                # Store the new forces
                forces[i] = new_forces

                #part of the code that calculates the evolution of a planet
                if(planet.evolucija2==0):
                    if(planet.poz[0]<0):
                        planet.evolucija2=planet.evolucija1
                    else:
                        planet.evolucija1=planet.evolucija1+self.dt

        # Plotting/evolucije
        for i in self.lista_planeta:
            print(i.ime,":",2*i.evolucija2/float(31556926),"god")
        plt.figure(figsize=(10, 10))
        for planet in self.lista_planeta:
            plt.plot(planet.lista_x, planet.lista_y, label=planet.ime)
        
        plt.xlabel('X Position (m)')
        plt.ylabel('Y Position (m)')
        plt.title('2D Orbits of Planets in the Solar System')
        plt.legend()
        plt.axis('equal')  # Ensure equal scaling on both axes
        plt.grid(True)
        plt.show()

    def calculate_net_force(self, planet, new_poz=None):
        if new_poz is None:
            new_poz = planet.poz

        net_force = np.array([0.0, 0.0])
        for other_planet in self.lista_planeta:
            if planet is not other_planet:
                r_vec = other_planet.poz - new_poz
                distance = np.linalg.norm(r_vec)
                if distance > 0:
                    force_magnitude = self.G * planet.M * other_planet.M / distance**2
                    force_direction = r_vec / distance
                    net_force += force_magnitude * force_direction
        return net_force
    def animate(self):
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(-5e12, 5e12)
        ax.set_ylim(-5e12, 5e12)
        ax.set_xlabel('X Position (m)')
        ax.set_ylabel('Y Position (m)')
        ax.set_title('2D Orbits of Planets in the Solar System')
        ax.grid(True)

        lines = [ax.plot([], [], 'o', label=planet.ime)[0] for planet in self.lista_planeta]
        ax.legend()

        def init():
            for line in lines:
                line.set_data([], [])
            return lines

        def update(frame):
            for line, data in zip(lines, self.steps_data):
                line.set_data(data[frame][0], data[frame][1])
            return lines

        anim = FuncAnimation(fig, update, frames=len(self.steps_data[0]), init_func=init, blit=False, interval=0.1)
        plt.show()
# Planets initialization
sunce = Planet("Sun", 0, 1.989 * 10**30, 0)
merkur = Planet("Mercury", 5.791 * 10**10, 3.3011 * 10**23, 47400)
venera = Planet("Venus", 1.082 * 10**11, 4.8675 * 10**24, 35000)
zemlja = Planet("Earth", 1.496 * 10**11, 5.97237 * 10**24, 29780)
mars = Planet("Mars", 2.279 * 10**11, 6.4171 * 10**23, 24070)
jupiter = Planet("Jupiter", 7.785 * 10**11, 1.8982 * 10**27, 13070)
saturn = Planet("Saturn", 1.433 * 10**12, 5.6834 * 10**26, 9680)
uranus = Planet("Uranus", 2.872 * 10**12, 8.6810 * 10**25, 6800)
neptun = Planet("Neptune", 4.495 * 10**12, 1.02413 * 10**26, 5400)

# Universe initialization and trajectory calculation
solarni_sistem = Svemir(500, 1 * 31556926, [sunce, merkur, venera, zemlja, mars, jupiter, saturn, uranus, neptun])
solarni_sistem.trajektorij()
solarni_sistem.animate()