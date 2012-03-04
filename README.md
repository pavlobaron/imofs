imofs - IMAP Based Online File Storage
==========

Did you know that IMAP is a pretty neat thing? It allows you to have
your email at one place and synchronize your PC, laptop, smartphone
and whatever you use for email with one central "repository". Well,
there is a bunch of drawbacks, especially when accessing your account
concurrently from different clients, but anyway it's cool.

IMAP basically works with emails. So, what actually is an email? If you think it's some electronic,
transferable text "containing" attachments, you are also right. But
for **imofs**, it's just a file enveloped in a message, stored in a
folder (mailbox).

So what **imofs** does is to save your files within a draft email on
the IMAP server. Subfolders (mailboxes) can be easily created, so we have a simple online file system.

Whatever device you have connected to the IMAP
server, it can see and even modifiy your folders (mailboxes). So you have a poor
guy's DropBox here. And yes, sharing would also work when you share
IMAP account cridentials with someone else. And there is enough
providers around offering you email accounts free of charge, so you
don't need to use your real one or limit your **imofs** use to only
one account. In the end, you can just subscribe to your folders
(mailboxes) in your IMAP client and sent messages as emails.

**imofs** is only limited by your quota, the expiration of your drafts and your
IMAP server capacity. Or however you call it. And by whatever
concurrency settings and limitations exist for your account.

And yes, I'm still learning to use Python in reasonable systems. Feel
free to point me at things I do completely wrong.

# Usage: #

Just fire `python imofs.py --help` for details.

# TODO: #

- rm and cp remote -> local not yet implemented - implement
- bigger set of options for UNIX style commands
- more intelligence when creating folders and copying files
- dealing with SSL
- implement rmdir
- deal with subfolders
- check / extend for email encoding
- implement mv - a combined cp and rm
- implement intelligent rewrite logic when the same file already exists
