Changelog
=========


1.0.14 (unreleased)
-------------------

- Nothing changed yet.


1.0.13 (2021-05-17)
-------------------

- Build more specific procedure interface
  [boulch]
- Remove useless index because template si specifying in zcml file
  [boulch]
- Add add_view Procedure expression
  [boulch]


1.0.12 (2021-05-04)
-------------------

- e_guichet field is printing like a link in template
  [boulch]

- Add new procedure validator
  [boulch]

- e_guichet field always available (even if imio.behavior.teleservice is installed)
  [boulch]

- Fix / update buildout & dependencies
  [laulaz]


1.0.11 (2021-01-06)
-------------------

- Remove lead-image out of procedure template
  [boulch]


1.0.10 (2020-08-12)
-------------------

- [WEB-3405] : Don't forget upgrade step to (re)change view on existing objects
  [boulch]

1.0.9 (2020-08-12)
------------------

- [WEB-3405] : First step :Change procedure default view.
  [boulch]


1.0.8 (2020-07-08)
------------------

- [WEB-3381] : Fix procedure contenttypes view when imio.behavior.teleservices isn't install.
  [boulch]


1.0.7 (2020-07-06)
------------------

- Override edit and add View : When ITsProcedure behavior is there, we want to hide e_guichet basic text field.
  [boulch]
- upgradesteps : To apply new default procedure template.
  [boulch]
- Procedure template : Change "a href" link to e-guichet by "button" to e-guichet.
  [boulch]
- Procedure template : (Add Leadimage fancybox, add RichText)
  [boulch]



1.0.6 (2020-07-01)
------------------

- Add custom "procedure_view" for content type "procedure".
  [boulch, laulaz]


1.0.5 (2020-01-14)
------------------

- Don't try to migrate related items in NavigationRoot and don't try to remove them.
  [boulch]


1.0.4 (2020-01-10)
------------------

- Refactoring setuphandlers. Remove old procedure at end of the process. Better manage for demarche (old_procedure) relatedItems
  [boulch]


1.0.3 (2020-01-07)
------------------

- Fix a bug when we get current wf state. We now use updateRoleMappingsFor to get good permissions and good roles in the current state. (products and procedure)
  [boulch]

- Add "procedure" content type + step to migrate old "demarche" document to procedure : WEBOTT-19
  [boulch]


1.0.2 (2019-03-18)
------------------

- Add icon for product content type : WEBOTT-10
  [laulaz]

- Add Fancybox overlay on product image : WEBOTT-10
  [laulaz]


1.0.1 (2019-03-18)
------------------

- Minor improvements (leadimage size & more css classes) : WEBOTT-10
  [laulaz]


1.0 (2019-02-05)
----------------

- Initial release.
  [laulaz]
