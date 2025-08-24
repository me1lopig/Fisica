# Create a more comprehensive version with additional astronomical examples
script_content_final = '# masa_estelar_astronomical.py - Calculadora de masa estelar con unidades astronómicas'

# Constantes físicas
G = 6.67430e-11  # m^3 kg^-1 s^-2 (constante gravitacional)
M_SUN = 1.98847e30  # kg (masa solar)

# Factores de conversión astronómicos
AU = 1.496e11  # m (1 Unidad Astronómica en metros)
KM_S_TO_M_S = 1000  # km/s a m/s

def calcular_masa(v_km_s, r_au):

    #Calcula la masa M de un cuerpo central dado:
      #v_km_s: velocidad orbital (km/s)
      #r_au: radio de la órbita (AU - Unidades Astronómicas)
    
    #Convierte a unidades SI y aplica la fórmula: M = v^2 * r / G
    #Devuelve masa en kg y en masas solares.

    # Conversión a unidades SI
    v_m_s = v_km_s * KM_S_TO_M_S  # km/s -> m/s
    r_m = r_au * AU  # AU -> m
    
    # Cálculo de la masa usando la tercera ley de Kepler modificada
    M_kg = v_m_s**2 * r_m / G
    M_solar = M_kg / M_SUN
    
    return M_kg, M_solar

def clasificar_estrella(M_solar):
    # Clasifica la estrella según su masa
    if M_solar < 0.08:
        return "enana marrón"
    elif M_solar < 0.5:
        return "enana roja"
    elif M_solar < 2:
        return "estrella tipo solar"
    elif M_solar < 8:
        return "estrella masiva"
    elif M_solar < 25:
        return "estrella muy masiva"
    else:
        return "estrella hipergigante"

def ejemplos_astronomicos():
    #Muestra ejemplos con datos reales del Sistema Solar
    print("=== Ejemplos con datos del Sistema Solar ===")
    
    planetas = [
        ("Mercurio", 47.87, 0.39),
        ("Venus", 35.02, 0.72),
        ("Tierra", 29.78, 1.00),
        ("Marte", 24.07, 1.52),
        ("Júpiter", 13.07, 5.20),
        ("Saturno", 9.69, 9.58),
        ("Urano", 6.81, 19.20),
        ("Neptuno", 5.43, 30.05)
    ]
    
    for nombre, v, r in planetas:
        M_kg, M_solar = calcular_masa(v, r)
        print(f"{nombre:8}: v={v:5.2f} km/s, r={r:5.2f} AU → M={M_solar:.4f} M☉")

def main():
    print("=== Calculadora de Masa Estelar ===")
    print("Usando unidades astronómicas estándar:")
    print("• Velocidad orbital: km/s")
    print("• Radio orbital: AU (Unidades Astronómicas)")
    print("• 1 AU = 149.6 millones de km (distancia Tierra-Sol)")
    print()
    
    try:
        # Lectura de datos por teclado
        v_km_s = float(input("Introduce la velocidad orbital v (km/s): "))
        r_au = float(input("Introduce el radio de la órbita r (AU): "))

        M_kg, M_solar = calcular_masa(v_km_s, r_au)

        print("\\" + "="*50)
        print("RESULTADOS:")
        print("="*50)
        print(f"Velocidad orbital: {v_km_s:.2f} km/s")
        print(f"Radio orbital: {r_au:.3f} AU ({r_au*149.6:.1f} millones de km)")
        print(f"Masa central: {M_kg:.6e} kg")
        print(f"             ≃ {M_solar:.3f} masas solares (M☉)")
        
        # Clasificación estelar
        clasificacion = clasificar_estrella(M_solar)
        print(f"Clasificación: {clasificacion}")
        
        # Comparaciones útiles
        print("\\Comparaciones:")
        if M_solar > 0.1:
            print(f"• {M_solar/1:.1f} veces la masa del Sol")
        if M_solar < 10:
            print(f"• {M_solar*1047:.0f} veces la masa de Júpiter")
            
    except KeyboardInterrupt:
        print("\\Cálculo interrumpido por el usuario.")
    except ValueError:
        print("\\Error: Por favor introduce valores numéricos válidos.")

if __name__ == "__main__":
    print("Modo interactivo:")
    main()
    print("\\" + "="*50)
    ejemplos_astronomicos()
