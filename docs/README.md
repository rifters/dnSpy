# dnSpy API Documentation Index

Welcome to the dnSpy API documentation. This comprehensive documentation covers all public APIs for developing dnSpy extensions.

## Documentation Structure

### [📘 API Documentation](API_DOCUMENTATION.md)
Complete guide to dnSpy's public APIs

**Contents:**
- Getting Started
- Extension Development Guide
- Core APIs (Menus, ToolBars, Commands, Settings)
- Tool Windows
- Document and Assembly APIs
- UI Components
- Complete Working Examples

**Best for:** Getting started with extension development, understanding the overall architecture, and finding comprehensive examples.

---

### [🐛 Debugger API](DEBUGGER_API.md)
Detailed reference for the debugger API

**Contents:**
- DbgManager - Core Debugging Interface
- Processes, Threads, and Runtimes
- Breakpoint Management
- Call Stack Navigation
- Expression Evaluation
- Step Debugging
- Exception Handling
- Advanced Debugging Techniques

**Best for:** Building debugging extensions, monitoring debug sessions, and working with the debugger programmatically.

---

### [⚙️ .NET Debugger API](DOTNET_DEBUGGER_API.md)
.NET-specific debugging features

**Contents:**
- .NET Runtime Interface
- .NET Code Locations
- .NET Expression Evaluation
- Type System (DmdType)
- Value Manipulation
- Metadata Access
- Decompiler Integration
- Async/Await Debugging

**Best for:** Working with .NET-specific debugging features, type inspection, and advanced .NET evaluation.

---

### [⚡ Quick Reference](QUICK_REFERENCE.md)
Concise reference with code snippets

**Contents:**
- Extension Setup Templates
- Menu Creation
- ToolBar Creation
- Command Registration
- Tool Windows
- Settings Management
- Common Debugger Operations
- Document Operations
- Essential Imports and Constants

**Best for:** Quick lookups, code snippets, and common patterns.

---

## Getting Started

### 1. Read the Basics
Start with the [API Documentation](API_DOCUMENTATION.md) to understand the fundamentals.

### 2. Explore Examples
Check out the example extensions:
- [`Extensions/Examples/Example1.Extension/`](../Extensions/Examples/Example1.Extension/) - Basic extension features
- [`Extensions/Examples/Example2.Extension/`](../Extensions/Examples/Example2.Extension/) - Advanced features

### 3. Use Quick Reference
Keep the [Quick Reference](QUICK_REFERENCE.md) handy while coding.

### 4. Dive Deep
For specific topics:
- **Debugging features?** → [Debugger API](DEBUGGER_API.md)
- **.NET-specific debugging?** → [.NET Debugger API](DOTNET_DEBUGGER_API.md)
- **Quick snippet?** → [Quick Reference](QUICK_REFERENCE.md)

---

## Common Tasks

### Creating a Menu Command
→ [API Documentation - Menu System](API_DOCUMENTATION.md#menu-system)  
→ [Quick Reference - Menus](QUICK_REFERENCE.md#menus)

### Adding a ToolBar Button
→ [API Documentation - ToolBar System](API_DOCUMENTATION.md#toolbar-system)  
→ [Quick Reference - ToolBars](QUICK_REFERENCE.md#toolbars)

### Creating a Tool Window
→ [API Documentation - Tool Windows](API_DOCUMENTATION.md#tool-windows)  
→ [Quick Reference - Tool Windows](QUICK_REFERENCE.md#tool-windows)

### Working with Assemblies
→ [API Documentation - Document and Assembly APIs](API_DOCUMENTATION.md#document-and-assembly-apis)  
→ [Quick Reference - Documents](QUICK_REFERENCE.md#documents)

### Debugging Operations
→ [Debugger API - DbgManager](DEBUGGER_API.md#dbgmanager)  
→ [Quick Reference - Debugger](QUICK_REFERENCE.md#debugger)

### Expression Evaluation
→ [Debugger API - Expression Evaluation](DEBUGGER_API.md#expression-evaluation)  
→ [.NET Debugger API - Expression Evaluation](DOTNET_DEBUGGER_API.md#net-expression-evaluation)

### Saving Settings
→ [API Documentation - Settings System](API_DOCUMENTATION.md#settings-system)  
→ [Quick Reference - Settings](QUICK_REFERENCE.md#settings)

---

## Key Namespaces

| Namespace | Purpose | Documentation |
|-----------|---------|---------------|
| `dnSpy.Contracts.Extension` | Extension infrastructure | [API Docs](API_DOCUMENTATION.md#extension-development) |
| `dnSpy.Contracts.Menus` | Menu system | [API Docs](API_DOCUMENTATION.md#menu-system) |
| `dnSpy.Contracts.ToolBars` | Toolbar system | [API Docs](API_DOCUMENTATION.md#toolbar-system) |
| `dnSpy.Contracts.Documents` | Assembly/Document management | [API Docs](API_DOCUMENTATION.md#document-and-assembly-apis) |
| `dnSpy.Contracts.Debugger` | Core debugger | [Debugger API](DEBUGGER_API.md) |
| `dnSpy.Contracts.Debugger.DotNet` | .NET debugging | [.NET Debugger API](DOTNET_DEBUGGER_API.md) |
| `dnSpy.Contracts.Settings` | Settings persistence | [API Docs](API_DOCUMENTATION.md#settings-system) |
| `dnSpy.Contracts.ToolWindows` | Tool window system | [API Docs](API_DOCUMENTATION.md#tool-windows) |

---

## Architecture Overview

```
┌─────────────────────────────────────────────┐
│           dnSpy Application                 │
└─────────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
┌───────▼────────┐    ┌────────▼──────────┐
│  Core Services │    │  Debugger Engine  │
│                │    │                   │
│  • Documents   │    │  • DbgManager     │
│  • Menus       │    │  • Breakpoints    │
│  • ToolBars    │    │  • Evaluation     │
│  • Settings    │    │  • Call Stack     │
│  • UI Controls │    │  • .NET Runtime   │
└────────┬───────┘    └────────┬──────────┘
         │                     │
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │  Public Contracts   │
         │  (Extension APIs)   │
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │  Your Extension     │
         │                     │
         │  • Menu Commands    │
         │  • Tool Windows     │
         │  • Debugger Hooks   │
         │  • Custom Features  │
         └─────────────────────┘
```

---

## Best Practices

### ✅ Do's
- Use MEF for dependency injection (`[Import]`, `[Export]`)
- Generate unique GUIDs for all components
- Dispose of resources properly
- Use the debugger dispatcher for debugger operations
- Cache expensive operations
- Handle errors gracefully
- Document your extension's public APIs

### ❌ Don'ts
- Don't forget to export types with `[Export]` attributes
- Don't block the UI thread
- Don't forget to unsubscribe from events
- Don't assume objects are non-null
- Don't use hard-coded paths or settings
- Don't call debugger APIs from wrong thread

---

## API Compatibility

These APIs are designed to be stable across dnSpy versions. However:
- Always target the same .NET Framework version as dnSpy
- Test your extension with each dnSpy release
- Avoid using internal APIs (not in `Contracts` namespaces)
- Subscribe to release notifications for breaking changes

---

## Support and Resources

- **GitHub Repository:** https://github.com/0xd4d/dnSpy
- **Wiki:** https://github.com/0xd4d/dnSpy/wiki
- **Example Extensions:** [`Extensions/Examples/`](../Extensions/Examples/)
- **Issue Tracker:** https://github.com/0xd4d/dnSpy/issues
- **License:** GPLv3

---

## Contributing to Documentation

Found an error or want to improve the documentation? Contributions are welcome!

1. Fork the repository
2. Make your changes
3. Submit a pull request

---

## Quick Links

### By Feature
- [Menus & Commands](API_DOCUMENTATION.md#menu-system) | [Quick Ref](QUICK_REFERENCE.md#menus)
- [ToolBars](API_DOCUMENTATION.md#toolbar-system) | [Quick Ref](QUICK_REFERENCE.md#toolbars)
- [Tool Windows](API_DOCUMENTATION.md#tool-windows) | [Quick Ref](QUICK_REFERENCE.md#tool-windows)
- [Debugging](DEBUGGER_API.md) | [Quick Ref](QUICK_REFERENCE.md#debugger)
- [Assemblies](API_DOCUMENTATION.md#document-and-assembly-apis) | [Quick Ref](QUICK_REFERENCE.md#documents)

### By Task
- [Create Extension](API_DOCUMENTATION.md#creating-your-first-extension)
- [Add Breakpoint](DEBUGGER_API.md#creating-breakpoints)
- [Evaluate Expression](DEBUGGER_API.md#expression-evaluation)
- [Load Assembly](API_DOCUMENTATION.md#working-with-documents)
- [Save Settings](API_DOCUMENTATION.md#settings-system)

---

**Happy Coding! 🚀**

For questions and support, please visit the [GitHub repository](https://github.com/0xd4d/dnSpy).
