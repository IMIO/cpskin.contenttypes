Changelog
=========


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
