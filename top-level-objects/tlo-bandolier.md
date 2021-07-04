## Description

Used to find information your character's Bandolier

## Forms

|          |                                                                         |
|----------|-------------------------------------------------------------------------|
| *Active* | True/False is XXX bandolier profile currently active?                   |
| *Index*  | Returns the index number of the Bandolier profile                       |
| *Item*   | Returns a bandolier item type which has 4 members: Index,ID,IconID,Name |
| *Name*   | Returns the named of the Bandolier profile                              |

## Methods

|            |                                |
|------------|--------------------------------|
| *Activate* | activate the bandolier profile |
|            |                                |

## Examples

  
/if (!${Me.Bandolier\[${Bandolier\[1HB\].Active}) {

  
/echo \[${Time}\] player want us to activate Bandolier: 1HB.

/invoke ${Me.Bandolier\[1HB\].Activate}

}

<!-- -->

  
/echo I have a ${Me.Bandolier\[1HB\].Item\[1\].Name} in my primary bandoilier slot

  
Output: I have a Snowreaver in my primary bandoilier slot

## See Also

-   [Top-Level Objects](top-level-objects.md)


