from django.db import models
from d_mm.models import MaterialStatus
from e_commodities.models import CommodityDetail
from g_measures.models import MilepostTemplate
from j_cb.models import CBWP


class ProjectComponent(models.Model):
    # A project component technically is a unique thing on a project, however we need the ability to reuse it
    # with the same identification across multiple functions. For e.g A pump "ABC-001" needs to be identified
    # and tracked during installation, but it 'may' need to be identified and tracked again during startup. These are
    # two separate activities with individual costs. For now, let us group the 'id' along with the 'function' for
    # uniqueness on the project.
    project_component_code = models.CharField(unique=True, max_length=25, verbose_name='Project Component Code')
    project_component_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                               verbose_name='Project Component Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Project Component Comments')

    # qty to be added here as this would represent client base quantities.

    class Meta:
        managed = True
        verbose_name_plural = "Project Components"
        db_table = 'project_component'
        app_label = 'k_quantum'
        ordering = ['project_component_code']

    def __str__(self):
        return str('%s' % self.project_component_code)


class ProjectDocument(models.Model):
    project_document_code = models.CharField(unique=True, max_length=25, verbose_name='Project Document Code')
    project_document_title = models.CharField(unique=True, max_length=100, verbose_name='Project Document Title')
    revision_number = models.CharField(max_length=3, blank=True, null=True, verbose_name='Revision No')
    revision_status = models.CharField(max_length=55, blank=True, null=True, verbose_name='Revision Status')
    release_date = models.DateTimeField(blank=True, null=True, verbose_name='Release Date')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Project Document Comments')
    document_attachment = models.FileField(blank=True, null=True, upload_to='Documents/',
                                           verbose_name='Document Attachment')
    document_url = models.URLField(blank=True, null=True, max_length=250,
                                   verbose_name='Document URL')

    class Meta:
        managed = True
        verbose_name_plural = "Project Documents"
        db_table = 'project_document'
        app_label = 'k_quantum'
        ordering = ['project_document_code']

    def __str__(self):
        return str('%s' % self.project_document_code)


class ProjectDocumentComponent(models.Model):
    # This is a junction table which joins a component with a document. It is the best form of uniqueness, but can be
    # overkill on some projects. The idea is to use (link) this unified widget in the csl_d_deliverables app for
    # tracking. The premise being that a unified_widget may still be on a very high level for tracking and may
    # need to be broken down some more for takeoff and tracking.
    project_document_component_code = models.CharField(unique=True, max_length=25,
                                                       verbose_name='Project Unified Document Component Code',
                                                       default='Test')
    project_document_component_title = models.CharField(unique=True, blank=True, null=True, max_length=100,
                                                        verbose_name='Project Unified Document Component Code Title')
    project_component = models.ForeignKey(ProjectComponent,
                                          on_delete=models.CASCADE, verbose_name='Project Component ID', default=1)
    project_document = models.ForeignKey(ProjectDocument,
                                         on_delete=models.CASCADE, verbose_name='Project Document ID', default=1)

    class Meta:
        managed = True
        verbose_name_plural = "Project Unified Documents Components"
        db_table = 'project_document_component'
        app_label = 'k_quantum'
        ordering = ['project_document_component_code']

    def __str__(self):
        return str('%s' % self.project_document_component_code)


class CBWPQuantum(models.Model):
    cbwp = models.ForeignKey(CBWP, on_delete=models.CASCADE, verbose_name='CBWP ID', default=1)
    project_document_component = models.ForeignKey(ProjectDocumentComponent, blank=True, null=True,
                                                   on_delete=models.CASCADE,
                                                   verbose_name='Project Document Component ID',
                                                   default=1)
    material_status = models.ForeignKey(MaterialStatus, on_delete=models.CASCADE,
                                        verbose_name='Material Status ID', default=1)
    commodity_detail = models.ForeignKey(CommodityDetail, on_delete=models.CASCADE,
                                         verbose_name='Commodity Detail ID', default=1)
    milepost_template = models.ForeignKey(MilepostTemplate, on_delete=models.CASCADE,
                                          verbose_name='Milepost Template ID', default=1)
    quantum_code = models.CharField(unique=True, max_length=100, verbose_name='CBWP Quantum Code')
    quantum_title = models.CharField(unique=True, max_length=255, blank=True, null=True,
                                     verbose_name='CBWP Quantum Title')
    cad_id = models.CharField(max_length=55, blank=True, null=True, verbose_name='CAD ID')
    quantity = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True, verbose_name='Quantity')
    mp_01_date_p = models.DateTimeField(verbose_name='1st Planned MP Date', blank=True, null=True, )
    mp_01_date_e = models.DateTimeField(verbose_name='1st Earned MP Date', blank=True, null=True, )
    mp_02_date_p = models.DateTimeField(verbose_name='2nd Planned MP Date', blank=True, null=True, )
    mp_02_date_e = models.DateTimeField(verbose_name='2nd Earned MP Date', blank=True, null=True, )
    mp_03_date_p = models.DateTimeField(verbose_name='3rd Planned MP Date', blank=True, null=True, )
    mp_03_date_e = models.DateTimeField(verbose_name='3rd Earned MP Date', blank=True, null=True, )
    mp_04_date_p = models.DateTimeField(verbose_name='4th Planned MP Date', blank=True, null=True, )
    mp_04_date_e = models.DateTimeField(verbose_name='4th Earned MP Date', blank=True, null=True, )
    mp_05_date_p = models.DateTimeField(verbose_name='05th Planned Milepost Date', blank=True, null=True, )
    mp_05_date_e = models.DateTimeField(verbose_name='05th Earned Milepost Date', blank=True, null=True, )
    mp_06_date_p = models.DateTimeField(verbose_name='06th Planned Milepost Date', blank=True, null=True, )
    mp_06_date_e = models.DateTimeField(verbose_name='06th Earned Milepost Date', blank=True, null=True, )
    mp_07_date_p = models.DateTimeField(verbose_name='07th Planned Milepost Date', blank=True, null=True, )
    mp_07_date_e = models.DateTimeField(verbose_name='07th Earned Milepost Date', blank=True, null=True, )
    mp_08_date_p = models.DateTimeField(verbose_name='08th Planned Milepost Date', blank=True, null=True, )
    mp_08_date_e = models.DateTimeField(verbose_name='08th Earned Milepost Date', blank=True, null=True, )
    mp_09_date_p = models.DateTimeField(verbose_name='09th Planned Milepost Date', blank=True, null=True, )
    mp_09_date_e = models.DateTimeField(verbose_name='09th Earned Milepost Date', blank=True, null=True, )
    mp_10_date_p = models.DateTimeField(verbose_name='10th Planned Milepost Date', blank=True, null=True, )
    mp_10_date_e = models.DateTimeField(verbose_name='10th Earned Milepost Date', blank=True, null=True, )
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "CBWP Quantum"
        db_table = 'cbwp_quantum'
        app_label = 'k_quantum'
        ordering = ['quantum_code']

    def __str__(self):
        return str('%s' % self.quantum_code)