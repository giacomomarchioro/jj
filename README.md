# jj (in development)
Incremental scripting module. Allows to use shell to write scripts based on the command history.

This module is very easy to use.
Import jj:

from jj import jj 

Start the logging:

jj.start()

Do all your experimenting in the shell.

Finally, write back the cleaned-up history of what you have done:

jj.write()

## Compared to similar alternatives 

import readline
readline.write_history_file('/home/ahj/history')




iPython magic function:
%save current_session ~0/
%save filename 1-48

jj is based on readline module but it adds clean-up features. 

