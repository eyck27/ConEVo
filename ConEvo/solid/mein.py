class Estudiante :
    def __init__ (self , codigo , nombre, email , carrera):
        self.codigo = codigo
        self.nombre = nombre
        self.email = email
        self.carrera = carrera
        self.notas =[]

    def agregar_notas (self , curso, nota , creditos):
        self.notas.append({
            "curso" : curso,
            "nota" : nota,
            "creditos" : creditos
        })

    def calcular_promedio_ponderado(self):
        if not self.notas:
            return 0
        suma_ponderada = sum(nota['nota']* nota['creditos']
                             for nota in self.notas)
        total_creditos = sum(nota['creditos'] for nota in self.notas)
        return suma_ponderada / total_creditos if total_creditos else 0

    def general_reporte_academico(self):  # usage
        reporte = f"=== REPORTE ACADÉMICO UNSCH ===\n"
        reporte += f"Estudiante: {self.nombre} ({self.codigo}) \n"
        reporte += f"Carrera: {self.carrera}\n"
        reporte += f"Email: {self.email}\n\n"
        reporte += "HISTORIAL ACADÉMICO:\n"

        for nota_info in self.notas:
            reporte += f"- {nota_info['curso']}: {nota_info['nota']} "
            reporte += f"({nota_info['creditos']} créditos)\n"

        reporte += f"\nPromedio Ponderado: {self.calcular_promedio_ponderado():.2f}"
        return reporte

    def enviar_email_notificacion(self, mensaje):  # usage
        # Simulación de envío de email
        print(f"Enviando email a {self.email}: {mensaje}")

        return True

    def guardar_en_base_datos(self):
        # Simulación de guardado en BD
        print(f"Guardando estudiante {self.codigo} en base de datos...")
        # Aquí iría la lógica real de persistencia
        return True

estudiante = Estudiante( "23231", "alex", "alex@p", "obstetricia")
estudiante.agregar_notas("extraccion renacuajos", 20, 5 )
estudiante.general_reporte_academico()
estudiante.enviar_email_notificacion("aprobaste ")
estudiante.guardar_en_base_datos()


print (estudiante.general_reporte_academico())

class Estudiante :
    def __init__ (self , codigo , nombre, email , carrera):
        self.codigo = codigo
        self.nombre = nombre
        self.email = email
        self.carrera = carrera

class RegistroAcademico:
    def __init__(self):
        self.notas = []

    def agregar_nota(self, curso, nota, creditos):
        self.notas.append({
            'curso': curso,
            'nota': nota,
            'creditos': creditos
        })

    def obtener_notas(self):
        return self.notas.copy()

class CalculadoraPromedio:
    @staticmethod
    def calcular_promedio_ponderado(notas):
        if not notas:
            return 0
    suma_ponderada = sum(nota["nota"]* nota ["creditos"] for nota in notas)
    total_creditos = sum(nota["creditos"] for nota in notas)
    return suma_ponderada / total_creditos if total_creditos > 0 else 0
class GeneradoReportes:

    def generar_reporte_estudiante(self,estudiante , registro_academico):
        promedio = CalculadoraPromedio.calcular_promedio_ponderado(
            registro_academico.obtener_notas()
        )
        reporte = f"=== REPORTE aCADEMICO UNSCH"