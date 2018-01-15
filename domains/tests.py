# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.contrib.auth.models import User

from domains.models import Domain, ForwardDomain

# Create your tests here.

class DomainTest(TestCase):
    def setUp(self):
            User.objects.create_user('test', 'test@user.com', 'test123')
            Domain.objects.create(name='test.com',owner_id='1')
            ForwardDomain.objects.create(name='forwardtest.com', owner_id='1', to_domain_id='1')

    def test_domain_exists(self):
        domain_lookup = Domain.objects.filter(name='test.com').count()
        self.assertEqual(domain_lookup,1)

    def test_forward_domain_exists(self):
        fwd_domain_lookup = ForwardDomain.objects.filter(name='forwardtest.com').count()
        self.assertEqual(fwd_domain_lookup, 1)

    def test_domain_delete(self):
        Domain.objects.get(name='test.com').delete()
        domain_lookup = Domain.objects.filter(name='test.com').count()
        self.assertEqual(domain_lookup,0)
        
    def test_forward_domain_delete(self):
        ForwardDomain.objects.get(name='forwardtest.com').delete()
        fwd_domain_lookup = ForwardDomain.objects.filter(name='forwardtest.com').count()
        self.assertEqual(fwd_domain_lookup,0)

