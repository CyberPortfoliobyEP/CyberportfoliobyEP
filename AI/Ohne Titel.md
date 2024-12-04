# Lab: Setting up ChatGPT via OpenAI API

## Lab Details

- **Lab Objective:** Understand how to set up and use the OpenAI API with ChatGPT for making requests and debugging.
- **Resources:**
  - **Machine:** Parrot Security OS
  - **OpenAI API Documentation:** [Making Requests](https://platform.openai.com/docs/api-reference/making-requests)
  - **Tools:**
    - OpenAI API
    - Shell (Terminal commands)
- **Preparation:** Ensure a valid OpenAI API key is generated and funds are added to the account for making requests.

---

## Introduction

This lab demonstrates the setup process for using the OpenAI API with ChatGPT. It covers generating an API key, installing the required tools, and sending basic API requests. ChatGPT provides multiple models under the API, but the focus here is on integrating it for simple queries.

---

## Step 1: Generate API Key and Configure Access

1. Navigate to the [OpenAI API page](https://platform.openai.com/account/api-keys).
2. Log in and create an API key. Copy the key securely for further use.
3. Ensure sufficient funds are added to your OpenAI account for API usage.

![OpenAI API Key Setup](https://i.imgur.com/DXnFtIf.png)

---

## Step 2: Install Necessary Tools

Run the following commands to install the required tools for API integration:

```bash
sudo apt install openai
```

---


## Explanation: Installs the OpenAI client library for interaction with the API.

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-YOUR_API_KEY" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7
  }'
```

**Explanation:** A sample request to test the OpenAI API with the gpt-4 model. Replace sk-YOUR_API_KEY with your generated API key.

---

## Step 3: Debugging and Verifying Setup

You can test if the API key works by sending a curl request:

```bash
curl -I https://api.openai.com/v1/chat/completions
```
**Result:** If configured correctly, you should receive a response with status code 200 OK. Any issues may return 404 Not Found or 500 Internal Server Error.

Screenshot API Key input + Verifying
[img](https://i.imgur.com/tROp1mB.png)
[img]([https://i.imgur.com/hS9A1ck.png)

---

## Summary

**Setup:** OpenAI API key creation, tool installation, and configuration.

**Execution:** A basic example of sending requests to ChatGPT via the OpenAI API.

**Conclusion:** With the OpenAI API properly set up, users can quickly integrate AI-powered tools into their workflows, simplifying tasks and generating responses programmatically.

```bash
Replace `https://example.com` placeholders with the actual links to your uploaded images/screenshots.
```
