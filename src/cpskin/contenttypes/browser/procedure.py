# -*- coding: utf-8 -*-

from imio.behavior.teleservices.behaviors.ts_procedure import ITsProcedure
from Products.Five import BrowserView


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
