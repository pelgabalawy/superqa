import os

regression_suite = [f for f in os.listdir("./regression/web_pages") if ".py" in f]
print("-- Regression Suite: " + str(regression_suite))

for testcase in regression_suite:
    print("---" + testcase + "---")
    os.system("pytest ./regression/web_pages/" + testcase)