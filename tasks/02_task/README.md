# Create a Simple NSO Service with Plan Component data

## Overview

This document provides a step-by-step guide to creating a simple NSO service package.  
The goal is to add plan components (`init` and `ready` states) upon deployment without modifying the existing service YANG model and Python code.

---

## Objectives

1. **Create a Basic NSO Service**  
   Generate a service package with minimal configuration.

2. **Add Plan Components**  
   Introduce `init` and `ready` plan states during service deployment.

3. **Preserve Existing Files**  
   Make no changes to the existing service YANG model file or service Python code.
