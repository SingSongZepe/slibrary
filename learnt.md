# learnt from the project

- never put anything in main thread, if it is not associated with Ui set-up
    > I set a SIGNAL_DOWNLOAD class to use main thread to download book
    > It is totally foolish

- may be it is better to use a dataclass to contain all the data need to be restored
    > use Slibrary to store the data, and when need to restore the data in json file
    > call its function - save
    > when call up, initialize with no parameters a Slibrary instance and then call its read function to get the data from json file