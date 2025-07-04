# 🔑 GitHub Personal Access Token Setup

## SSH Failed - Using HTTPS with Token Instead

Since SSH keys aren't set up, let's use HTTPS with a Personal Access Token:

### Step 1: Create Personal Access Token

1. **Open this link**: https://github.com/settings/tokens
2. **Click**: "Generate new token" → "Generate new token (classic)"
3. **Fill out the form**:
   - **Note**: `sentiment-analysis-upload`
   - **Expiration**: `30 days` (or longer if you prefer)
   - **Scopes**: ✅ Check `repo` (this gives full repository access)
4. **Click**: "Generate token"
5. **IMPORTANT**: Copy the token immediately! You won't see it again.

### Step 2: Use Token to Push

After creating your token, run:

```bash
git push -u origin main
```

**When prompted for credentials:**
- **Username**: `Panchadip-128`
- **Password**: `ghp_xxxxxxxxxxxxxxxxxxxx` (your token)

### Step 3: Store Token (Optional)

To avoid entering it every time:

```bash
git config --global credential.helper store
```

Then the next time you push, it will save your credentials.

### Alternative: Use Token in URL

You can also embed the token in the remote URL:

```bash
git remote set-url origin https://ghp_YOUR_TOKEN_HERE@github.com/Panchadip-128/sentiment_analysis_google_reviews.git
git push -u origin main
```

Replace `ghp_YOUR_TOKEN_HERE` with your actual token.

## Quick Test Command

```bash
# Test if you can push now
git push -u origin main
```
