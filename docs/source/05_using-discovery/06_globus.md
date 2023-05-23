(using-globus)=

# Using Globus

Globus is a data management system that you can use to transfer and share files.
Northeastern has a subscription to Globus, and you can setup a Globus account with
your Northeastern credentials. If you have another account, either personal or
through another institution, you can also link your accounts.

To use Globus, you must first set up an account as detailed below. Then, you must install Globus Connect to create an endpoint on your local computer, as also detailed below.
After you have completed these two initial setup procedures, you can then use the Globus web app to perform file transfers. See :ref: `using_nuendpoint` for a walkthrough of using the Northeastern endpoint on Globus.

## Globus Account Set Up

Use the following instructions to setup an account with Globus using your Northeastern credentials.

1. Go to [Globus](https://www.globus.org).
2. Click **Log In**.
3. From the Use your existing organizational login, select **Northeastern University**, and then click **Continue**.
4. Enter your Northeastern username and password.
5. If you do not have a previous Globus account, click **Continue**. If you have a previous account, click Link to existing account.
6. Check the agreement checkbox, and then click **Continue**.
7. Click **Allow** to give Globus permissions to access your files.

You will then be able to access the [Globus File Manager app](https://app.globus.org).

:::{tip}
If you received an account identity that includes your NUID number
(for example <000123456@northeastern.edu>), you can follow the “Creating and linking
a new account identity” instructions below to get a different account identity if
you want a more user-friendly account identity. You can then link the two accounts together.
:::

### Creating and linking a new account identity (Optional)

If you created an account through the Northeastern University existing organizational
login and received a username that includes your NUID, you can create a new identity
with a different username and then link the two accounts together. A username that you have selected,
as opposed to one with your NUID, can make it easier for you to remember your login credentials.

1. Go to [Globus](https://www.globus.org).
2. Click **Log In**.
3. Click **Globus ID** to sign in.
4. Click **Need a Globus ID? Sign up**.
5. Enter your Globus ID information.
6. Enter the verification code that Globus sends to your email.
7. Click **Link to an existing account** to link this new account with your primary account.
8. Select Northeastern University from the dropdown box, and click **Continue** to be taken to the Northeastern University single sign on page.
9. Enter your Northeastern username and password.

You should now be able to see your two accounts linked in the Account section on the [Globus web app](https://app.globus.org/account/identities).

## Install Globus Connect Personal (GCP)

Use Globus Connect Personal (GCP) to use your personal laptop as an endpoint.
You first need to install GCP using the following procedure.
You need to be logged into Globus before you can install GCP.

1. Go to [Globus File Manager](https://app.globus.org/file-manager/gcp).
2. Enter a name for your endpoint in the Endpoint Display Name field.
3. Click **Generate Setup Key** to generate a setup key for your endpoint.
4. Click the **Copy** icon next to the setup key that was generated to copy the key to your clipboard. You will need this key during the installation of GCP in step 6.
5. Click the appropriate OS icon for your computer to download the installation file.
6. After the installation file has been downloaded to your computer, double click on the file to launch the installer.

Accept the defaults on the install wizard. After the install completes, you can now use your laptop as an endpoint within Globus.

:::{note}
You can't modify an endpoint after you have created it. If you need an endpoint with different options, you'll need to completely delete
the endpoint and recreate it. Follow the instructions on the Globus website for [deleting and recreating an endpoint](https://docs.globus.org/faq/globus-connect-endpoints/#how_do_i_get_a_new_setup_key_for_a_reinstallation_of_globus_connect_personal).
:::

## Working with Globus

After you have an account and set up a personal endpoint using Globus Connect personal, you can perform basic file management tasks using the Globus File Manager interface
such as transferring files, renaming files, and creating new folders. You can also download and use the Globus Command Line Interface (CLI) tool. Globus also has extensive documentation and
training files for you to practice with.

(using-nuendpoint)=

### Using the Northeastern endpoint

To access the Northeastern endpoint on Globus, on the Globus web app, click **File Manager**, then in the **Collection** text box, type Northeastern. The endpoints owned by Northeastern University display in the collection area.
The general Northeastern endpoint is `northeastern#discovery`.
Using the File Manager interface, you can easily change directories, switch the direction of transferring to and from, and specify options such as transferring only new or changed files. Below is a procedure for transferring files from Discovery to your
personal computer, but with the flexibility of the File Manager interface, you can adjust the endpoints, file view, direction of the transfer, and many other options.

**To transfer files from Discovery to your personal computer, do the following**

1. Create an endpoint on your computer using the procedure above "Install Globus Connect", if you have not done so already.
2. In the File Manager on the Globus web app, in the **Collections** textbox, type Northeastern, then in the collection list click the `northeastern#discovery` endpoint.
3. In the right-pane menu, click **Transfer or Sync to**.
4. Click in the **Search** text box, and then in on the **Your Collections** tab, click the name of your personal endpoint. You now can see the list of your files on Discovery on the left and a list of your files on your personal computer on the right.
5. Select the file or files from the right-side list of Discovery files that you want to transfer to your personal computer.
6. Select the destination folder from the left-side list of the files on your personal computer.
7. (Optional) Click **Transfer & Sync Options** and select the transfer options that you need.
8. Click **Start**.

### Connecting to Google Drive

The version of Globus currently on Discovery allows you to connect to Google Drive by first setting up the connection in GCP. This will add your Google Drive to your current personal endpoint.
You'll need to first have a personal endpoint, as outlined in the procedure above.This procedure is slightly different from using the Google Drive Connector with
Globus version 5.5. You'll need your Google Drive [downloaded to your local computer](https://www.google.com/drive/download/).

**To add Google Drive to your personal endpoint, do the following**

1. Open the GCP app. On Windows, right click on the **G** icon in your taskbar and select **Options**. On Mac, click the **G** icon in the menu bar and select **Preferences**.
2. On the **Access** tab, click the + button to open the **Choose a directory** dialog box.
3. Navigate to your Google Drive on your computer and click **Choose**.
4. Click the **Shareable** checkbox to make this a shareable folder in Globus File Manager, and then click **Save**.

You can now go to Globus File Manager and see that your Google Drive is available as a folder on your personal endpoint.

### Command Line Interface (CLI)

The Globus Command Line Interface (CLI) tool allows you to access Globus from a command line. It is a stand-alone app that requires a separate download
and installation. Please refer to the [Globus CLI documentation](https://docs.globus.org/cli/) for working with this app.

### Globus documentation and test files

Globus provides detailed instructions on using Globus and also has test files for you to practice with.
These are free for you to access and use. We encourage you to use the test files to become familiar with the Globus interface.
You can access the Globus documentation and training files on the [Globus How To website](https://docs.globus.org/how-to/).
