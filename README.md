## Setup

* Initialize the submodules
```bash
git submodule init
git submodule update
```

* Install the requirements
```bash
conda create -n venv python=3.10
conda activate venv
pip install -r requirements.txt

# To evaluate on AgentBench
pip install -r evaluator/agentbench/AgentBench/requirements.txt
pip install -r evaluator/agentbench/AgentBench/src/tasks/knowledgegraph/requirements.txt
pip install -r evaluator/agentbench/AgentBench/src/tasks/lateralthinkingpuzzle/requirements.txt
```

* Finetune with QLoRA quantization
```bash
export HUGGINGFACE_API_TOKEN=<API_TOKEN>
python llama2_qlora.py configs/<filename>.yaml
```
