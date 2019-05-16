from django.test import Client, TestCase
from django.urls import reverse

from . import views
# Create your tests here.
from .models import Mineral

client = Client()

class MineralModelTests(TestCase):
    """ unit test for the db """
    def test_mineral_creation(self):
        """ tests creation of mineral objects:

        asserts correct type, instance of, and contains
        """
        mineral = Mineral.objects.create(
            name='trace mineral',
            image_filename="240px-Abernathyite%2C_Heinrichite-497484.jpg,",
            image_caption='Pale yellow abernathyite crystals and green '
                          'heinrichite crystals',
            category='Arsenate',
            formula='K(UO<sub>2</sub>)('
                    'AsO<sub>4</sub>)·<sub>3</sub>H<sub>2</sub>O',
            strunz_classification='08.EB.15',
            color='Yellow',
            crystal_system='Tetragonal',
            unit_cell='a = 7.176Å, c = 18.126ÅZ = 4',
            crystal_symmetry='H-M group: 4/m 2/m 2/mSpace group: P4/ncc',
            cleavage='Perfect on {001}',
            mohs_scale_hardness='2.5–3',
            luster='Sub-Vitreous, resinous, waxy, greasy',
            streak='Pale yellow',
            diaphaneity='Transparent',
            optical_properties='Uniaxial (-)',
            refractive_index='nω = 1.597 – 1.608nε = 1.570',
            crystal_habit='Lath - shaped like a small, thin plaster lath, '
                          'rectangular in shape',
            specific_gravity='2.88',
            group='trace group'
            )
        self.assertIsInstance(mineral, Mineral)
        self.assertTrue(mineral, type(object))
        self.assertTrue(hasattr(mineral, 'crystal_symmetry'))


class MineralViewsTests(TestCase):
    """ tests for views"""
    def setUp(self):
        """ setup for tests to instantiate mineral objects to test against"""
        self.mineral = Mineral.objects.create(
            name='trace mineral',
            image_filename="240px-Abernathyite%2C_Heinrichite-497484.jpg,",
            image_caption='Pale yellow abernathyite crystals and green '
                          'heinrichite crystals',
            category='Arsenate',
            formula='K(UO<sub>2</sub>)('
                    'AsO<sub>4</sub>)·<sub>3</sub>H<sub>2</sub>O',
            strunz_classification='08.EB.15',
            color='Yellow',
            crystal_system='Tetragonal',
            unit_cell='a = 7.176Å, c = 18.126ÅZ = 4',
            crystal_symmetry='H-M group: 4/m 2/m 2/mSpace group: P4/ncc',
            cleavage='Perfect on {001}',
            luster='Sub-Vitreous, resinous, waxy, greasy',
            streak='Pale yellow',
            diaphaneity='Transparent',
            optical_properties='Uniaxial (-)',
            refractive_index='nω = 1.597 – 1.608nε = 1.570',
            crystal_habit='Lath - shaped like a small, thin plaster lath, '
                          'rectangular in shape',
            specific_gravity='2.88',
            group='trace group'
            )

        self.mineral2 = Mineral.objects.create(
            name='Emily Mineral',
            image_filename="240px-Abernathyite%2C_Heinrichite-497484.jpg,",
            image_caption='Pale yellow abernathyite crystals and green '
                          'heinrichite crystals',
            category='Arsenate',
            formula='K(UO<sub>2</sub>)('
                    'AsO<sub>4</sub>)·<sub>3</sub>H<sub>2</sub>O',
            strunz_classification='08.EB.15',
            color='Yellow',
            crystal_system='Tetragonal',
            unit_cell='a = 7.176Å, c = 18.126ÅZ = 4',
            crystal_symmetry='H-M group: 4/m 2/m 2/mSpace group: P4/ncc',
            cleavage='Perfect on {001}',
            mohs_scale_hardness='2.5–3',
            luster='Sub-Vitreous, resinous, waxy, greasy',
            streak='Pale yellow',
            diaphaneity='Transparent',
            optical_properties='Uniaxial (-)',
            refractive_index='nω = 1.597 – 1.608nε = 1.570',
            crystal_habit='Lath - shaped like a small, thin plaster lath, '
                          'rectangular in shape',
            specific_gravity='2.88',
            group='team trimily'
        )

    def test_minerals_list_view(self):
        """
            unit test for index view logic

            asserts correct status code,  context,,
            template rendered, and contains

        """
        resp = self.client.get(reverse('trace_minerals:trace_minerals_index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'trace_minerals/index.html')
        self.assertContains(resp, self.mineral.name)

    def test_minerals_glossary_view(self):
        """
            unit test for glossary view logic

            asserts correct status code,  context,,
            template rendered, and contains and
            query contents and number of queries
            to db

        """
        resp = self.client.get('/glossary/', {'char':'p'})
        self.assertEquals(resp.status_code, 200)
        context = resp.context['minerals']
        self.assertEqual(resp.resolver_match.func, views.mineral_glossary)
        self.assertTemplateUsed(resp, 'trace_minerals/index.html')

    def test_minerals_search_view(self):
        """
            unit test for search view logic

            asserts correct status code,  context,,
            template rendered, and contains and
            query contents and number of queries
            to db

        """
        resp = self.client.get('/search/', {'q':'allophane'})
        self.assertEquals(resp.status_code, 200)
        #context = resp.context['minerals']
        self.assertEqual(resp.resolver_match.func, views.mineral_search)
        self.assertTemplateUsed(resp, 'trace_minerals/index.html')

    def test_minerals_group_view(self):
        """
            unit test for search view logic

            asserts correct status code,  context,,
            template rendered, and contains and
            query contents and number of queries
            to db

        """
        resp = self.client.get('/group/', {'group':'Halides'})
        self.assertEquals(resp.status_code, 200)
        #context = resp.context['minerals']
        self.assertEqual(resp.resolver_match.func, views.mineral_group)
        self.assertTemplateUsed(resp, 'trace_minerals/index.html')

    def test_mineral_detail_view(self):
        """
                    unit test for detail view logic

                    asserts correct status code, context,
                    and that pk is present

                """
        resp = self.client.get(reverse('trace_minerals:trace_minerals_detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
