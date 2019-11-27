# -*- coding: utf-8 -*-

from plone import api
from plone.app.textfield.value import RichTextValue
from plone.namedfile.file import NamedBlobImage
import logging
import unidecode

logger = logging.getLogger('cpskin.contenttypes')


def post_install(context):
    """We need to migrate existing TTW content types if any"""
    migrate_product(context)
    migrate_procedures(context)


def migrate_procedures(context):
    # keywords (DEMARCHE)
    portal_types = api.portal.get_tool(name='portal_types')
    existing_brains = []
    # new type Procedure.
    if "Procedure" not in portal_types:
        import ipdb; ipdb.set_trace()  # noqa
        context.runImportStepFromProfile("profile-cpskin.contenttypes:default", "typeinfo")
        context.runImportStepFromProfile("profile-cpskin.contenttypes:default", "rolemap")

    # types to migrate
    if 'demarche' in portal_types:
        existing_brains = api.content.find(portal_type='demarche')
    else:
        existing_document_brains = api.content.find(portal_type='Document')
        for brain in existing_document_brains:
            for tag in brain.isearchTags:
                if "DEMARCHE" in unidecode.unidecode(tag).upper():
                    existing_brains.append(tag)
    for brain in existing_brains:
        old_procedure = brain.getObject()
        container = old_procedure.aq_parent
        new_id = old_procedure.id
        temp_id = 'new-{0}'.format(new_id)
        # new type "Procedure"
        new_procedure = api.content.create(
            container=container,
            type='Procedure',
            id=temp_id,
            title=old_procedure.Title(),
            safe_id=False,
        )
        new_procedure.description = old_procedure.Description()
        if hasattr(old_procedure, "e_guichet"):
            new_procedure.e_guichet = old_procedure.e_guichet
        if old_procedure.texte:
            new_procedure.text = RichTextValue(
                raw=old_procedure.texte.raw,
                mimeType=old_procedure.texte.mimeType,
                outputMimeType=old_procedure.texte.outputMimeType,
            )
        new_procedure.effective_date = old_procedure.effective_date
        new_procedure.creation_date = old_procedure.creation_date
        modification_date = old_procedure.modification_date
        new_procedure.workflow_history = old_procedure.workflow_history
        new_procedure.creators = old_procedure.creators
        new_procedure.language = old_procedure.language
        new_procedure.modification_date = modification_date
        new_procedure.reindexObject(idxs=['modified'])

        # restore workflow state
        state = api.content.get_state(old_procedure)
        api.content.transition(obj=new_procedure, to_state=state)

        api.content.delete(obj=old_procedure, check_linkintegrity=True)
        api.content.rename(obj=new_procedure, new_id=new_id, safe_id=True)
        new_procedure.reindexObject()

        new_procedure.modification_date = modification_date
        new_procedure.reindexObject(idxs=['modified'])
        logger.info('Migrated procedure {0}'.format(new_procedure.absolute_url()))
    if 'demarche' in portal_types:
        del portal_types['demarche']


def migrate_product(context):
    """Existing TTW 'produit' content type migration"""
    portal_types = api.portal.get_tool(name='portal_types')
    if 'produit' not in portal_types:
        return

    existing_brains = api.content.find(portal_type='produit')
    for brain in existing_brains:
        old_product = brain.getObject()
        container = old_product.aq_parent
        new_id = old_product.id
        temp_id = 'new-{0}'.format(new_id)
        new_product = api.content.create(
            container=container,
            type='Product',
            id=temp_id,
            title=old_product.Title(),
            safe_id=False,
        )

        # copy standard fields / values
        new_product.description = old_product.Description()
        new_product.price = old_product.prix
        new_product.size = old_product.taille_s
        new_product.color = old_product.couleur_s
        if old_product.informations:
            new_product.informations = RichTextValue(
                raw=old_product.informations.raw,
                mimeType=old_product.informations.mimeType,
                outputMimeType=old_product.informations.outputMimeType,
            )
        new_product.effective_date = old_product.effective_date
        new_product.creation_date = old_product.creation_date
        modification_date = old_product.modification_date
        new_product.workflow_history = old_product.workflow_history
        new_product.creators = old_product.creators
        new_product.language = old_product.language

        # copy leadimage
        old_image = old_product.image
        if old_image:
            filename = old_image.filename
            old_image_data = old_image.data
            namedblobimage = NamedBlobImage(
                data=old_image_data,
                filename=filename,
            )
            setattr(new_product, 'image', namedblobimage)

        # restore workflow state
        state = api.content.get_state(old_product)
        api.content.transition(obj=new_product, to_state=state)

        api.content.delete(obj=old_product, check_linkintegrity=True)
        api.content.rename(obj=new_product, new_id=new_id, safe_id=True)
        new_product.reindexObject()

        new_product.modification_date = modification_date
        new_product.reindexObject(idxs=['modified'])

        logger.info('Migrated product {0}'.format(new_product.absolute_url()))

    del portal_types['produit']
