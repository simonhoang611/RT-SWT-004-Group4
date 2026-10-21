# Guide to running H2 (C1 zero-shot, C2 changed examples) on a Windows computer

English translation (19 Oct 2026, prepared with an AI assistant, Claude) of the Vietnamese original `HUONG_DAN_CHAY_H2.md` (SHA-256 69139c9ba367593e…), which the authors keep unchanged.

Script: `RBL-to-commit\revision\h2\h2_run_prompts.py` (SHA-256 `f6341309…67fef`, checked to match the version Claude tested).
The script keeps the model `gpt-5.4-mini-2026-03-17`, temperature 0, the system message and the output cleaning the same as in the original run. Only the examples in the prompt change.

**Do not edit the script, do not change the model.** If there is an error, copy the error message and send it to Claude.

## Step 0. Check Python (do this once)

Open **PowerShell** (click Start, type `PowerShell`, Enter), then type:

```powershell
python --version
```

- If it shows `Python 3.x.x` (3.9 or later), that is fine.
- If it says the command `python` is not recognized, try `py --version`. If this command works, replace `python` with `py` in every step below.
- If neither works: install Python from python.org. During installation, **tick the box "Add python.exe to PATH"**, then close PowerShell and open it again.

## Step 1. Install the openai library (do this once)

```powershell
python -m pip install openai
```

## Step 2. Go to the repo folder

```powershell
cd C:\Users\hoang\Downloads\RBL\RBL-to-commit
```

All the following commands are run from this folder.

## Step 3. Enter the API key (each time you open a new PowerShell window)

```powershell
$env:OPENAI_API_KEY = Read-Host "OpenAI key"
```

Paste the key when asked, then press Enter.
- This way the key is **not saved** in any file or in the command history. When the window is closed, the key is gone.
- Do **not** type the key directly into a command, and do not paste the key into the script or into the chat.

## Step 4. Trial run with 3 stories (1 story per domain)

```powershell
python revision\h2\h2_run_prompts.py --condition C1 --ids 1,101,201
python revision\h2\h2_run_prompts.py --condition C2 --ids 1,101,201
```

Each command must print exactly the following:

```
1/3 id=1 OK
2/3 id=101 OK
3/3 id=201 OK
Finished. 3 rows, not OK: []
```

If so, go to Step 5. If not, see the section "If you get an error" below. These three trial rows **are kept**: the full run will skip them automatically, because the configuration is identical.

## Step 5. Full run of 261 stories

```powershell
python revision\h2\h2_run_prompts.py --condition C1
python revision\h2\h2_run_prompts.py --condition C2
```

- Each command calls the API at most 261 times. The original run took about 35 minutes for 261 calls, so each condition may take about that long.
- You can open **two PowerShell windows** to run C1 and C2 in parallel. In the second window you must redo Step 2 and Step 3.
- Keep the computer from going to sleep during the run.
- **If the run is interrupted** (network lost, window closed by mistake, computer turned off): open it again, do Steps 2 and 3, then run **exactly the same command as before**. The script automatically skips the ids that are already OK and continues with the rest.
- When finished, the last line must be `Finished. 261 rows, not OK: []`. If there are still ids inside the brackets, run exactly that command once more: the script only reruns the ids that are not yet OK.

Estimated cost (rough, at the Standard price of $0.75 / $4.50 per 1M tokens): C1 about 2 USD, C2 about 2.5 USD. The C2 prompt is longer because the Fineract example (id 119) is about 30,000 characters long. The real figures will be recomputed from the logs after the run.

## Step 6. Tell Claude

There is no need to send files: Claude reads the folder `RBL-to-commit\revision\h2\` directly on your computer. When finished there will be 6 files:

| File | Content |
|---|---|
| `h2_C1_output.csv`, `h2_C2_output.csv` | Output for each id (id, status, generated_gherkin) |
| `h2_C1_api_log.jsonl`, `h2_C2_api_log.jsonl` | Log of each call: the model returned by the API, tokens, time, the error if any |
| `h2_C1_config.json`, `h2_C2_config.json` | Configuration of the most recent run |

**Do not open the CSV files in Excel and then save them again**, because Excel can damage the format. If you want to look at them, only open them to view, then close without saving.

## If you get an error

| Message | What to do |
|---|---|
| `Set OPENAI_API_KEY in the environment first.` | Step 3 has not been done in this window. |
| `ModuleNotFoundError: No module named 'openai'` | Redo Step 1 (if you use `py`, type `py -m pip install openai`). |
| `can't open file ... h2_run_prompts.py` | You are not in the right folder. Redo Step 2. |
| An `ERROR` line with `AuthenticationError` / `401` | The key is wrong or has expired. Enter the key again in Step 3, then run the command again. |
| An `ERROR` line with `RateLimitError` / `insufficient_quota` | The account is out of money or over its limit. Add funds or wait, then run exactly the same command again. |
| An `ERROR` line with `model_not_found` | The account cannot use this snapshot. **Do not change the model**; tell Claude. |
| Any other error | Copy the full message and send it to Claude. |

An `ERROR` line does not break anything. The script records `ERROR` with an empty output, never makes up an output by itself, and the next run will try that id again.
