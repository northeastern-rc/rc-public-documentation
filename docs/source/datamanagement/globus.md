(using-globus)=

# Using Globus

Globus is a data management system that you can use to transfer and share files. Northeastern has a subscription to Globus, and you can set up a Globus account with your Northeastern credentials. You can link your accounts if you have another account, either personal or through another institution.

To use Globus, you will need to set up an account, as detailed below. Then, as detailed below, you will need to install Globus Connect to create an endpoint on your local computer. After completing these two initial setup procedures, you can use the Globus web app to perform file transfers. See {ref}`using-nuendpoint` for a walkthrough of using the Northeastern endpoint on Globus.

## Globus Account Set Up

You can use the following instructions to set up an account with Globus using your Northeastern credentials.

1. Go to [Globus](https://www.globus.org).
1. Click **Log In**.
1. From the Use your existing organizational login, select **Northeastern University**, and then click **Continue**.
1. Enter your Northeastern username and password.
1. If you do not have a previous Globus account, click **Continue**. If you have a previous account, click the Link to an existing account.
1. Check the agreement checkbox, and then click **Continue**.
1. Click **Allow** to permit Globus to access your files.

You can then access the [Globus File Manager app](https://app.globus.org).

:::{tip}
If you received an account identity that includes your NUID number (for example, <000123456@northeastern.edu>), you can follow the “Creating and linking a new account identity” instructions below to get a different account identity if you want a more user-friendly account identity. You can then link the two accounts together.
:::

### Creating and linking a new account identity (Optional)

If you created an account through Northeastern University's existing organizational login and received a username that included your NUID, you can create a new identity with a different username and link the two accounts together. A username you select instead of one with your NUID can make it easier to remember your login credentials.

1. Go to [Globus](https://www.globus.org).
1. Click **Log In**.
1. Click **Globus ID** to sign in.
1. Click **Need a Globus ID? Sign up**.
1. Enter your Globus ID information.
1. Enter the verification code that Globus sends to your email.
1. Click **Link to an existing account** to link this new account with your primary account.
1. Select Northeastern University from the drop-down box and click **Continue** to be taken to the Northeastern University single sign-on page.
1. Enter your Northeastern username and password.

You should now see your two accounts linked in the Account section on the [Globus web app](https://app.globus.org/account/identities).

## Install Globus Connect Personal (GCP)

Use Globus Connect Personal (GCP) as an endpoint for your laptop. You first need to install GCP using the following procedure and be logged in to Globus before you can install GCP.

1. Go to [Globus File Manager](https://app.globus.org/file-manager/gcp).
1. Enter a name for your endpoint in the Endpoint Display Name field.
1. Click **Generate Setup Key** to generate a setup key for your endpoint.
1. Click the **Copy** icon next to the generated setup key to copy the key to your clipboard. You will need this key during the installation of GCP in step 6.
1. Click the appropriate OS icon for your computer to download the installation file.
1. After downloading the installation file to your computer, double-click on the file to launch the installer.

Accept the defaults on the install wizard. After the installation, you can use your laptop as an endpoint within Globus.

:::{note}
You cannot modify an endpoint after you have created it. If you need an endpoint with different options, you must delete and recreate it. Follow the instructions on the Globus website for [deleting and recreating an endpoint](https://docs.globus.org/faq/globus-connect-endpoints/#what_are_globus_connect_personal_and_globus_connect_server).
:::

## Working with Globus

After you have an account and set up a personal endpoint using Globus Connect personal, you can perform basic file management tasks using the Globus File Manager interface, such as transferring files, renaming files, and creating new folders. You can also download and use the Globus Command Line Interface (CLI) tool. Globus also has extensive documentation and training files for you to practice with.

(using-nuendpoint)=

### Using the Northeastern endpoint

To access the Northeastern endpoint on Globus, on the Globus web app, click **File Manager**, then in the **Collection** text box, type Northeastern. The endpoints owned by Northeastern University are displayed in the collection area. The general Northeastern endpoint is `northeastern#discovery`. Using the File Manager interface, you can easily change directories, switch the direction of transferring to and from, and specify options such as transferring only new or changed files. Below is a procedure for transferring files from Discovery to your personal computer, but with the flexibility of the File Manager interface, you can adjust the endpoints, file view, direction of the transfer, and many other options.

**To transfer files from Discovery to your personal computer, do the following**

1. Create an endpoint on your computer using the procedure above "Install Globus Connect," if you have not done so already.
1. In the File Manager on the Globus web app, in the **Collections** textbox, type Northeastern, then in the collection list, click the `northeastern#discovery` endpoint.
1. click **Transfer or Sync to** in the right-pane menu.
1. Click in the **Search** text box, and then click the name of your endpoint on the **Your Collections** tab. You can now see the list of your files on Discovery on the left and on your personal computer on the right.
1. Select the file or files from the right-side list of Discovery files that you want to transfer to your personal computer.
1. Select the destination folder from the left-side list of the files on your computer.
1. (Optional) Click **Transfer & Sync Options** and select the transfer options you need.
1. Click **Start**.

### Connecting to Google Drive

The version of Globus currently on Discovery allows you to connect to Google Drive by first setting up the connection in GCP. This will add your Google Drive to your current personal endpoint.
Just so you know, you will first need a personal endpoint, as outlined in the procedure above. This procedure is slightly different from using the Google Drive Connector with
Globus version 5.5. You will need your Google Drive [downloaded to your local computer](https://www.google.com/drive/download/).

**To add Google Drive to your endpoint, do the following**

1. Open the GCP app. Right-click the **G** icon in your taskbar on Windows and select **Options**. Click the **G** icon in the menu bar on Mac and select **Preferences**.
1. On the **Access** tab, click the + button to open the **Choose a directory** dialog box.
1. Navigate to your Google Drive on your computer and click **Choose**.
1. Click the **Shareable** checkbox to make this a shareable folder in Globus File Manager, and then click **Save**.

You can now go to Globus File Manager and see that your Google Drive is available as a folder on your endpoint.

### Command Line Interface (CLI)

The Globus Command Line Interface (CLI) tool allows you to access Globus from the command line. It is a stand-alone app that requires a separate download
and installation. Please refer to the [Globus CLI documentation](https://docs.globus.org/cli/) for working with this app.

### Globus documentation and test files

Globus provides detailed instructions on using Globus and has test files for you to practice with. These are free for you to access and use. We would like to encourage you to use the test files to become familiar with the Globus interface. You can access the Globus documentation and training files on the [Globus How To website](https://docs.globus.org/how-to/).
