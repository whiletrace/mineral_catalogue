from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from .models import Mineral

# todo class Model_tests will inherit from TestCase
#  test to make sure that model Minerals
#  a new instance of mineral
#  test that minerals attr are of the correct type

class MineralModelTests(TestCase):

    def test_mineral_creation(self):
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


# todo test custom migration
#   incoming data format is json
#   deserialized format is type object
#   deserialized data populates Model Minerals

# todo class view_tests: index
#   Assert query provides a list of minerals
#   assert view uses proper URL
#   assert that proper var are passed through context
#   assert value of var passed through context is expected val
#   assert that proper template is rendered by view
class MineralViewsTests(TestCase):

    def setUp(self):
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
        resp = self.client.get(reverse('trace_minerals:trace_minerals_index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'trace_minerals/index.html')
        self.assertContains(resp, self.mineral.name)

# todo class view_tests:detail
#   Assert query provides a list of minerals
#   assert view uses proper URL
#   assert that proper var are passed through context
#   assert value of var passed through context is expected val
#   assert that proper template is rendered by view
    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('trace_minerals:trace_minerals_detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
