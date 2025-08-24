# masa_estelar_input.py

# Constante de gravitación universal en SI
G = 6.67430e-11  # m^3 kg^-1 s^-2

def calcular_masa(v, r):
    """
    Calcula la masa M de un cuerpo central dado:
      v: velocidad orbital (m/s)
      r: radio de la órbita   (m)
    Fórmula: M = v^2 * r / G
    Devuelve masa en kg.
    """
    return v**2 * r / G

def main():
    print("Cálculo de masa estelar a partir de velocidad y radio orbital")
    # Lectura de datos por teclado
    v = float(input("Introduce la velocidad orbital v (m/s): "))
    r = float(input("Introduce el radio de la órbita r (m): "))

    M = calcular_masa(v, r)
    Msol=1.989e30
    Mcomparada=M/Msol


    print("\nResultados:")
    print(f"  v = {v:.3e} m/s")
    print(f"  r = {r:.3e} m")
    print(f"  Masa central M = {M:.6e} kg")
    print(f"  Masa central M = {Mcomparada:.6e} masas solares")

if __name__ == "__main__":
    main()