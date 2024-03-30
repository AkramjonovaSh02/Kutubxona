from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    guruh = models.CharField(max_length=50)
    kurs = models.PositiveSmallIntegerField(choices=(
        (1,1),
        (2,2),
        (3,3),
        (4,4)
    ))
    k_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"

        unique_together = ('ism', 'kurs')

class Muallif(models.Model):
    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=10, choices=(
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol')
    ))
    tugilgan_sana = models.DateField(null=True, blank=True)
    kitoblar_soni = models.PositiveSmallIntegerField(null=True, blank=True)
    tirik = models.BooleanField()

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "Muallif"

        verbose_name_plural = "Mualliflar"

class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=255, null=True, blank=True )
    sahifa = models.PositiveSmallIntegerField(null=True, blank=True)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=255)
    ish_vaqti = models.CharField(max_length=20)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "Kutubxonachi"
        verbose_name_plural = "Kutubxonachilar"

class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.CASCADE)
    olingan_sana = models.DateField(auto_now_add=True)
    qaytardi = models.BooleanField(default=False)
    qaytarish_sana = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Recordlar"









