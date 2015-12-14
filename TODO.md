Sql Client
----

- [ ] Define Connection (dynamic/generated form, from connection string format)
- [ ] Open & Maintain Connection
- [ ] Ability to write sql (Scintilla Widget?)
- [ ] Ability to execute sql
  - [ ] Single (Defualt)
  - [ ] Entire Buffer (Modifier Key)
  - [ ] Query Logging
- [ ] Ability to quickly interrupt sql (Without prompting for new credentials)
- [ ] Database table browsers with current user permissions icons

MySQL Editor Features
----
- [ ] Host transaction restrictive tunnel.
  
    WrenchSQL can host and listen for inbound mysql connections. (Possible conifrm inbound connections, via gui)
    When established WrenchSQL allows a passthough of all mysql commands.
    Modes:
    - Regular: Block transaction state-chaning commands, return error.
    - Allow: Do not block any sql commands.
    - Whitlist: Only allow approved command stanzas.
    - Blacklist/Block:  Forbid forbidden command stanzas.
    - Off: Block all.
    
    Purpose:

    > Offer developer method of running non-transactional sql in a monitored transaction such that the WrnchSQL gui can also view changes made by the script and will host the transactional connection for as long as desired.
- [ ] Automatically Add/Remove commas in Select/Set Statements
- [ ] MySQL func Autocomplete
- [ ] Date/Time Picker?
- [ ] Automatically reorder out-of-order SQL statementes (Limit <//> group by)
- [ ] Automatic FK join autocomplete
- [ ] Gammer-aware autocorrect `like =` becomes `like`, `selectt` becomes `select`
- [ ] automatic explain warnings?

Dataview features:
----

 - [ ] View column as bar graph (compare values)
