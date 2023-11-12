# Expense report

`expense-report.py` is the script we use to generate our expense reports.

Currently, we use QuickBooks. The script is run on the output from Expenses > All transactions > Year to Date > Export.

Those exports are then provided to the script like so...

```bash
python3 PATH_TO_CSV
```

The goal is to update the report monthly. The [latest](./latest.csv) report is tracked as well as [previous](./archive/) reports.

# Contributing

If you think it's cool that we publish our financial data, why not be a part of it?!

Jokes aside, many thanks for any and all support!

### Paypal

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=NGEL6AB5A6KNL)

### [Venmo](https://venmo.com/empathetech)

### [Cash App](https://cash.app/$empathetech)

### [Patreon](https://patreon.com/empathetech)

### [Buy Me a Coffee](https://www.buymeacoffee.com/empathetech)

### [Ko-fi](https://ko-fi.com/empathetech)

# License

[GNU GPLv3](LICENSE)
