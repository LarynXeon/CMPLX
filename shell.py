import os
import atexit
from basic import run
from curtime import fr_dt

if not os.path.exists("logs"):
    os.makedirs("logs")

loptfl = os.path.join("logs", fr_dt)

with open(loptfl, 'w') as LOG:
        LOG.write("$ Session Start \n \n")

        while True:
            text = input("CMPLX > ")
            result, error = run('<stdin>', text)

            if text.strip() == 'exit':
                LOG.write("\n$ Session ended by user.\n")
                LOG.write("$ Script interrupted. Logs may be incomplete.\n")
                LOG.write("$ Script interrupted. Saving logs... \n")
                print("\n Script interrupted. Saving logs...")
                print("\n Logs saved.")
                print("\n Closing Program.")
                if not LOG.closed:
                    LOG.close()
                break

            if error:
                print(error.as_string())
            else:
                print(result)
                
                LOG.write(f'prompt - {text} \n')
                LOG.write(f'console - {result} \n\n')
