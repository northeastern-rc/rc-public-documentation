(ml-model-checkpointing)=
# ML Model-Level Checkpointing

Model-level checkpointing is a technique used to periodically save the state of a machine learning (ML) model during training, enabling the training process to be resumed from the saved checkpoint in case of interruptions or premature termination. The saved state typically includes the model's parameters, optimizer state, and essential training information (e.g., the epoch number and loss value). Model checkpoints are especially critical for long-running training jobs.

## Why is Checkpointing Important in Deep Learning?

Checkpointing allows you to resume the model's current state if the training process is interrupted due to hardware or software issues. You can also use checkpointing to save the best-performing model and load that for evaluation.

## TensorFlow Checkpoint Example

The following example implements a longer ML job using the [*tf.keras* checkpointing API](https://www.tensorflow.org/tutorials/keras/save_and_load) and multiple shorter Slurm job arrays on the GPU partition using the `submit_tf_array.bash` script:

:::{code} shell
#!/bin/bash
#SBATCH --job-name=myrun
#SBATCH --time=00:10:00
#SBATCH --partition=gpu,lowpriority
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --mem=10Gb
#SBATCH --output=%A-%a.out
#SBATCH --error=%A-%a.err
#SBATCH --array=1-10%1  #execute 10 array jobs, 1 at a time.

module load miniconda3/2020-09
source activate tf_gpu

# Define the number of steps based on the job id:
numOfSteps=$(( 500 * SLURM_ARRAY_TASK_ID ))

# Run python and save outputs to a log file corresponding to the current job task ID
python train_with_checkpoints.py $numOfSteps &> log.$SLURM_ARRAY_TASK_ID
:::

The following checkpoint example is given in the program `train_with_checkpoints.py`:

:::{code} python
checkpoint_path = "training_2/{epoch:d}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path,
    verbose=1,
    save_weights_only=True,
    period=5)
:::

[You can check out the RC Training Checkpointing scripts](https://github.com/northeastern-rc/training-checkpointing/tree/main/Exercise_2), which are modified from [TensorFlow Save and load models](https://www.tensorflow.org/tutorials/keras/save_and_load).

The Slurm option `--array=1-10%1` will create 10 Slurm array tasks and run one task at a time. Note that the saved variable `%A` denotes the main job ID, while variable `%a` denotes the task ID (spanning values 1-10). Note that the output/error files are also unique to prevent different jobs from writing to the same files. The Shell variable `SLURM_ARRAY_TASK_ID` holds the unique task ID value and can be used within the Slurm Shell script to point to different files or variables. To submit this job to the scheduler, use the command:

:::{code} shell
sbatch submit_tf_array.bash
:::

## PyTorch Checkpoint Example

### Setting up a Sample Project

You can set up a sample project to demonstrate checkpointing in PyTorch by creating a simple neural network and training it on a sample dataset. Use the following code to set up your simple neural network:

:::{code} python
import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.fc2 = nn.Linear(128, 10)
    def forward(self, x):
        x = x.view(-1, 28 * 28)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
:::

Once the neural network is defined, you can load a sample dataset and train the model. In this example, you will use the MNIST dataset in the `torchvision` library. The following code loads the MNIST dataset and trains the model:

:::{code} python
import torchvision
import torchvision.transforms as transforms

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
net = Net()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

for epoch in range(2):
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    print('Epoch %d loss: %.3f' % (epoch + 1, running_loss / len(trainloader)))
:::

### What is the Model State in PyTorch?

In PyTorch, the model state refers to the values of all the parameters, weights, and biases that define the model's behavior. This state is stored in the model's `state_dict`, a dictionary-like object that maps each layer to its parameter tensors. Additionally, the `state_dict` contains information about the model's architecture and the values of the parameters learned during training.

The `state_dict` can be saved to a file using PyTorch's `torch.save` function and loaded back into memory using `torch.load`. This allows for checkpointing, which saves the state of a model periodically during training so that it can be recovered in the case of a crash or interruption.

PyTorch also provides the ability to save and load the entire model, including the model's architecture and optimizer state, using the `torch.save` and `torch.load` functions. This allows for complete checkpointing of a model's state.

It is important to note that the `state_dict` only contains information about the model's parameters, not the optimizer or other training-related information. So, to save the optimizer state, you also need to save it separately and load it back when loading the model.

In conclusion, the model state in PyTorch represents the values of all the parameters, weights, and biases that define the model's behavior. The state is stored in the `state_dict` and can be saved and loaded for checkpointing purposes. By saving the model state periodically during training, you can ensure that your progress is recovered during a crash or interruption.

## Saving a PyTorch Model

### Saving a Model's state_dict

To save the learnable parameters of a PyTorch model and the optimizer, save the model's `state_dict`. Use the `torch.save` function to pass the `state_dict` and file names as arguments. The following code demonstrates how to save the `state_dict` of the model:

:::{code} python
checkpoint_path = 'checkpoint.pth'
state = {'epoch': epoch + 1,
         'state_dict': net.state_dict(),
         'optimizer': optimizer.state_dict()}
torch.save(state, checkpoint_path)
:::

### Saving the Entire Model

The entire model includes the architecture, the learnable parameters, and the optimizer state. Use the `torch.save()` function to save the entire model by passing the model and a filename as arguments:

:::{code} python
model_path = 'model.pth'
torch.save(net, model_path)
:::

:::{note}
When saving the entire model, the custom classes used to define the model must be importable, either as a part of the project or in a separate file that can be imported.
:::

(load-pytorch-model)=
## Loading a PyTorch Model

### Loading a PyTorch state_dict

The `torch.load` function will load the `state_dict` of a saved model by passing the file name as an argument. After loading the `state_dict`, we can set the `state_dict` of the model using the `model.load_state_dict` method:

:::{code} python
checkpoint = torch.load(checkpoint_path)
net.load_state_dict(checkpoint['state_dict'])
optimizer.load_state_dict(checkpoint['optimizer'])
epoch = checkpoint['epoch']
:::

### Loading the Entire PyTorch Model

To load the entire model, use the `torch.load` function and pass the file name as an argument. The loaded model can then be assigned to a variable, as shown in the following code:

:::{code} python
loaded_model = torch.load(model_path)
:::

### Resuming Training from a Checkpoint

To resume training from a checkpoint, you can use the following code which will load the model's `state_dict` and the optimizer's state and resume your training from the `epoch` value saved in the checkpoint file:

:::{code} python
checkpoint = torch.load(checkpoint_path)
net.load_state_dict(checkpoint['state_dict'])
optimizer.load_state_dict(checkpoint['optimizer'])
epoch = checkpoint['epoch']

# Continue training
for epoch in range(epoch, num_epochs):
    # Train the model
    # ...

    # Save the checkpoint
    state = {'epoch': epoch + 1,
             'state_dict': net.state_dict(),
             'optimizer': optimizer.state_dict()}
    torch.save(state, checkpoint_path)
:::

After each epoch, the model's `state_dict` and the optimizer's state will be saved in the checkpoint file.

## Model-Level Tips and Tricks

### Save Only the Model's State_dict

Save only the model's `state_dict` and optimizer state, which is the information needed to resume training. This reduces the checkpoint file's size and makes it easier to load the model.

### Save to Multiple Locations

Save the checkpoint file to multiple locations, such as a local drive and the cloud, to ensure that the checkpoint is recovered in case of failure.

### Use the Latest Versions of Libraries

Changes in libraries may cause compatibility issues with older checkpoints.

### Naming Conventions

Use a consistent naming convention for checkpoint files; include information such as the date, time, and epoch number in the file name to make tracking multiple checkpoint files easier and ensure you choose the proper checkpoint to load.

### Checkpoint Validation

Validate the checkpoint after loading it to ensure that the model's `state_dict` and the optimizer's state are correctly loaded by making a prediction using the loaded model and checking that the results are as expected.

### Periodic Clean-up

Remove old checkpoint files to avoid filling up storage. This can be done by keeping only the latest checkpoint or keeping only checkpoint files from the last few epochs.

### Document Checkpoints

Document the purpose of each checkpoint and what it contains: the model architecture, the training data, the hyperparameters, and the performance metrics. This will help keep track of the progress and make it easier to compare different checkpoints.
