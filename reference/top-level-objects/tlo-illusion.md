---
tags:
    - tlo
---
# `Illusion`

<!--tlo-desc-start-->
Used to get information about items on your illusions keyring.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
/// member | keyring Illusion
Access to the illusion keyring.
///

/// member | keyringitem Illusion[N]
Retrieves the item in your illusion keyring by index.
///

/// member | keyringitem Illusion[Name]
Retrieve the item in your illusion keyring by name. A `=` can be prepended for an exact match.
///
<!--tlo-forms-end-->

## Associated DataTypes
<!--tlo-datatypes-start-->
## [keyring](../data-types/datatype-keyring.md)
{%
  include-markdown "reference/data-types/datatype-keyring.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-keyring.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-keyring.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-keyring.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}

## [keyringitem](../data-types/datatype-keyringitem.md)
{%
  include-markdown "reference/data-types/datatype-keyringitem.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-keyringitem.md') }}
:    <h2>Members</h2>
    {%
    include-markdown "reference/data-types/datatype-keyringitem.md"
    start="<!--dt-members-start-->"
    end="<!--dt-members-end-->"
    heading-offset=0
    %}
    {%
    include-markdown "reference/data-types/datatype-keyringitem.md"
    start="<!--dt-linkrefs-start-->"
    end="<!--dt-linkrefs-end-->"
    %}
<!--tlo-datatypes-end-->

## Usage

See Also: [DataType:keyring](../data-types/datatype-keyring.md) and [DataType:keyringitem](../data-types/datatype-keyring.md)
<!--tlo-linkrefs-start-->
[keyring]: ../data-types/datatype-keyring.md
[keyringitem]: ../data-types/datatype-keyringitem.md
<!--tlo-linkrefs-end-->
