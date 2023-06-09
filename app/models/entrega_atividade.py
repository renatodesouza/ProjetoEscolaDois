from django.db import models
from .atividade import Atividade
from .aluno import Aluno
from .professor import Professor



class EntregaAtividade(models.Model):
    ENTREGUE = 'ENt'
    CORRIGIDO = 'COr'
    PENDENTE = 'PEn'

    escolha_status = [(ENTREGUE, 'Entregue'), (CORRIGIDO, 'Corrigido'), (PENDENTE, 'Pendente')]

    titulo = models.CharField(max_length=100)
    resposta = models.TextField(max_length=255, blank=True)
    status = models.CharField(max_length=3, choices=escolha_status, default=PENDENTE)
    nota = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    atividade = models.OneToOneField(Atividade, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    dt_entrega = models.DateField()
    dt_avaliacao = models.DateField()
    observacao = models.TextField(max_length=255)
    file = models.FileField(upload_to='file', null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Entrega da Atividade'  

    def __str__(self):
        return self.atividade.titulo