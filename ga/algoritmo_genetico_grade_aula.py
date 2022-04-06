class Data:
    SALAS = [[1, "LAB1"],[2, "LAB2"],
             [3, "LAB3"],[4, "LAB4"],
             [5, "LAB5"]]

    PROFESSORES = [[1, "FREDSON"],[2, "JANIO"],
                   [3, "SILVANO"],[4, "MARCO"],
                   [5, "TAYSE"],[6, "LEANDRA"],
                   [7, "TAMIRYS"],[8, "DOUGLAS"]]

    DIAS_SEMANAS = [[1, "SEGUNDA"],[2, "TERCA"],
                    [3, "QUARTA"],[4, "QUINTA"],
                    [5, "SEXTA"],[6, "SABADO"]]
    
    MATERIAS = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

class Populacao:
    pass

class AlgoritmoGenetico:
    pass

class Materia:
    def __init__(self, id ,nome, professor):
        self._id = id
        self._nome = nome
        self._professor = professor
    
    def get_id(self): return self._id
    def get_nome(self): return self._nome
    def get_professor(self): return self._professor
    def __str__(self): return self._nome

class Professor:
    def __init__(self, id, nome):
        self._id = id
        self._nome = nome
    def get_id(self): return self._id
    def get_nome(self): return self._nome
    def __str__(self): return self._nome

class Sala:
    def __init__(self, id, numero):
        self._id = id
        self._numero = numero
    def get_id(self): return self._id
    def get_numero(self): return self._numero
    def __str__(self): return self._numero

class DiaSemana:
    def __init__(self, id, dia):
        self._id = id
        self._dia = dia
    def get_id(self): return self._id
    def get_nome(self): return self._dia
    def __str__(self): return self._dia

class Aula:
    def __init__(self, id, materia):
        self._id = id
        self._materia = materia
        self._professor = None
        self._sala = None
        self._DiaSemana = None
        self._Periodo = None

    def get_id(self): return self._id
    def get_materia(self): return self._materia
    def get_professor(self): return self._professor
    def get_sala(self): return self._sala
    def get_DiaSemana(self): return self._DiaSemana
    def set_professor(self, professor): self._professor = professor 
    def set_sala(self, sala): self._sala = sala 
    def set_DiaSemana(self, DiaSemana): self._DiaSemana = DiaSemana 
    def __str__(self):
        return str(self._materia.get_nome()) + "," + str(self._sala.get_numero()) + "," + str(self._professor.get_nome()) + "," + str(self._DiaSemana.get_dia())

class Grade:
    def __init__(self, id):
        self._id = id
        self._aula
        pass
    