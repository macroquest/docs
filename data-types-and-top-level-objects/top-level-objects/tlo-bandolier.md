# TLO:Bandolier

## Description

Used to find information your character's Bandolier

## Forms

|  |  |
| :--- | :--- |
| _Active_ | True/False is XXX bandolier profile currently active? |
| _Index_ | Returns the index number of the Bandolier profile |
| _Item_ | Returns a bandolier item type which has 4 members: Index,ID,IconID,Name |
| _Name_ | Returns the named of the Bandolier profile |

## Methods

|  |  |
| :--- | :--- |
| _Activate_ | activate the bandolier profile |
|  |  |

## Examples

/if (!${Me.Bandolier[${Bandolier\[1HB].Active}) {

/echo [${Time}] player want us to activate Bandolier: 1HB.

/invoke ${Me.Bandolier[1HB].Activate}

}

/echo I have a ${Me.Bandolier[1HB\].Item\[1].Name} in my primary bandoilier slot

Output: I have a Snowreaver in my primary bandoilier slot

## See Also

* [Top-Level Objects](./)

