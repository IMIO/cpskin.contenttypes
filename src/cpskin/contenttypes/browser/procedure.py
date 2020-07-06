# -*- coding: utf-8 -*-

from imio.behavior.teleservices.behaviors.ts_procedure import ITsProcedure
from plone.app.contenttypes.behaviors.leadimage import ILeadImage
from plone.dexterity.browser import add
from plone.dexterity.browser import edit
from plone.dexterity.interfaces import IDexterityFTI
from Products.Five import BrowserView
from zope.component import queryUtility


class ProcedureView(BrowserView):
    """
    """

    def is_ts_behavior_is_install(self):
        if ITsProcedure.providedBy(self.context) is True:
            # Don't print e_guichet field
            return False
        elif self.context.e_guichet is None:
            # Don't print e_guichet field
            return False
        else:
            return True
class ProcedureEditForm(edit.DefaultEditForm):
    # if behavior is install so we hide default e_guichet field.
    def updateWidgets(self):
        super(ProcedureEditForm, self).updateWidgets()
        if ITsProcedure.providedBy(self.context):
            self.widgets['e_guichet'].mode = 'hidden'


class CustomAddForm(add.DefaultAddForm):
    portal_type = 'Procedure'

    def updateWidgets(self):
        super(CustomAddForm, self).updateWidgets()
        # When we add new contentype object, our behavior doesn't exist yet
        # So we search ITsProcedure in FTI
        if self.has_behavior("Procedure", "imio.behavior.teleservices.behaviors.ts_procedure.ITsProcedure"):
            self.widgets['e_guichet'].mode = 'hidden'

    def has_behavior(self, type_name, behavior_name):
        """Check if a behavior is on portal_type"""
        fti = queryUtility(IDexterityFTI, name=type_name)
        if not fti:
            return
        behaviors = list(fti.behaviors)
        if behavior_name not in behaviors:
            return False
        else:
            return True


class AddView(add.DefaultAddView):
    form = CustomAddForm
