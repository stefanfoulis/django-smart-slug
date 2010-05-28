import datetime
from django.test import TestCase

from testapp.models import Simple, Complex, UnderscoresNumerals

class SimpleTest(TestCase):
    def test_simple(self):
        s1 = Simple(slug='simple')
        s1.save()
        self.assertEqual(s1.slug, 'simpl')

        s2 = Simple(slug='simple')
        s2.save()
        self.assertEqual(s2.slug, 'simp_')

        s3 = Simple(slug='simple')
        s3.save()
        self.assertEqual(s3.slug, 'sim__')

    def test_date_handling(self):
        dt = datetime.datetime(2010, 1, 1, 1, 1, 1)
        c1 = Complex(
            title='complex example',
            pub_date=dt)
        c1.save()

        self.assertEqual(c1.slug, 'complex')

        dt = datetime.datetime(2010, 1, 2, 1, 1, 1)
        c2 = Complex(
            title='complex example',
            pub_date=dt)
        c2.save()

        self.assertEqual(c2.slug, 'complex')

        c3 = Complex(
            title='complex example',
            pub_date=dt)
        c3.save()
        
        self.assertEqual(c3.slug, 'complex_')

    def test_split_words_generation(self):
        dt = datetime.datetime(2010, 1, 1, 1, 1, 1)
        c1 = Complex(title='complex example', pub_date=dt)
        c1.save()
        self.assertEqual(c1.slug, 'complex')

        c2 = Complex(title='complex example', pub_date=dt)
        c2.save()
        self.assertEqual(c2.slug, 'complex_')

        c3 = Complex(title='complex example', pub_date=dt)
        c3.save()
        self.assertEqual(c3.slug, 'complex__')
        
        c4 = Complex(title='complex example', pub_date=dt)
        c4.save()
        self.assertEqual(c4.slug, 'complex___')
        
        c5 = Complex(title='complex example', pub_date=dt)
        c5.save()
        self.assertEqual(c5.slug, 'comple____')

    def test_complex_splitting(self):
        dt = datetime.datetime(2010, 1, 1, 1, 1, 1)
        c1 = Complex(title='complex example test', pub_date=dt)
        c1.save()

        self.assertEqual(c1.slug, 'complex')

        c1.title = "complexexample test"
        c1.save()
        self.assertEqual(c1.slug, 'complexexa')

        c2 = Complex(title='complexexample test', pub_date=dt)
        c2.save()
        self.assertEqual(c2.slug, 'complexex_')

        c3 = Complex(title='complexexample test', pub_date=dt)
        c3.save()
        self.assertEqual(c3.slug, 'complexe__')

    def test_numeral_handling(self):
        un1 = UnderscoresNumerals(slug_underscores='test', slug_numerals='test')
        un1.save()

        self.assertEqual(un1.slug_underscores, 'test')
        self.assertEqual(un1.slug_numerals, 'test')

        un2 = UnderscoresNumerals(slug_underscores='test', slug_numerals='test')
        un2.save()

        self.assertEqual(un2.slug_underscores, 'test_')
        self.assertEqual(un2.slug_numerals, 'test-1')

        un3 = UnderscoresNumerals(slug_underscores='test', slug_numerals='test')
        un3.save()

        self.assertEqual(un3.slug_underscores, 'test__')
        self.assertEqual(un3.slug_numerals, 'test-2')
