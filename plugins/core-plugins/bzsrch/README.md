---
tags:
   - plugin
---
# Bzsrch
<!--desc-start-->
This plugin adds bazaar search access and commands.
<!--desc-end-->

## Commands

<a href="bzsrch/">
{% 
  include-markdown "plugins/core-plugins/bzsrch/bzsrch.md" 
  start="<!--cmd-syntax-start-->" 
  end="<!--cmd-syntax-end-->" 
%}
</a>
:    {% include-markdown "plugins/core-plugins/bzsrch/bzsrch.md" 
        start="<!--cmd-desc-start-->" 
        end="<!--cmd-desc-end-->" 
        trailing-newlines=false 
     %} {{ readMore('plugins/core-plugins/bzsrch/bzsrch.md') }}

<a href="breset/">
{% 
  include-markdown "plugins/core-plugins/bzsrch/breset.md" 
  start="<!--cmd-syntax-start-->" 
  end="<!--cmd-syntax-end-->" 
%}
</a>
:    {% include-markdown "plugins/core-plugins/bzsrch/breset.md" 
        start="<!--cmd-desc-start-->" 
        end="<!--cmd-desc-end-->" 
        trailing-newlines=false 
     %} {{ readMore('plugins/core-plugins/bzsrch/breset.md') }}

<a href="bzquery/">
{% 
  include-markdown "plugins/core-plugins/bzsrch/bzquery.md" 
  start="<!--cmd-syntax-start-->" 
  end="<!--cmd-syntax-end-->" 
%}
</a>
:    {% 
     include-markdown "plugins/core-plugins/bzsrch/bzquery.md" 
     start="<!--cmd-desc-start-->" 
     end="<!--cmd-desc-end-->" 
     trailing-newlines=false 
     %} {{ readMore('plugins/core-plugins/bzsrch/bzquery.md') }}

## Top-Level Objects

## [Bazaar](bzsrch-tlo-bazaar.md)
{%
  include-markdown "plugins/core-plugins/bzsrch/bzsrch-tlo-bazaar.md"
  start="<!--tlo-desc-start-->"
  end="<!--tlo-desc-end-->"
  trailing-newlines=false
%} {{ readMore('plugins/core-plugins/bzsrch/bzsrch-tlo-bazaar.md') }}

<h2>Forms</h2>
{%
  include-markdown "plugins/core-plugins/bzsrch/bzsrch-tlo-bazaar.md"
  start="<!--tlo-forms-start-->"
  end="<!--tlo-forms-end-->"
  heading-offset=0
%}
{% 
  include-markdown "plugins/core-plugins/bzsrch/bzsrch-tlo-bazaar.md" 
  start="<!--tlo-linkrefs-start-->"
  end="<!--tlo-linkrefs-end-->"
%}

## Datatypes

## [bazaar](bzsrch-datatype-bazaar.md)
{%
  include-markdown "plugins/core-plugins/bzsrch/bzsrch-datatype-bazaar.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('plugins/core-plugins/bzsrch/bzsrch-datatype-bazaar.md') }}

<h2>Members</h2>
{%
  include-markdown "plugins/core-plugins/bzsrch/bzsrch-datatype-bazaar.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "plugins/core-plugins/bzsrch/bzsrch-datatype-bazaar.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

## [bazaaritem](bzsrch-datatype-bazaaritem.md)
{%
  include-markdown "plugins/core-plugins/bzsrch/bzsrch-datatype-bazaaritem.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('plugins/core-plugins/bzsrch/bzsrch-datatype-bazaaritem.md') }}

<h2>Members</h2>
{%
  include-markdown "plugins/core-plugins/bzsrch/bzsrch-datatype-bazaaritem.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "plugins/core-plugins/bzsrch/bzsrch-datatype-bazaaritem.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%} 
