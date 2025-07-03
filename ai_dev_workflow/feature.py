#!/usr/bin/env python3
"""
Feature Markdown Generator

This script generates structured feature markdown files based on project 
configuration and user input. It creates task breakdowns tailored to the
project type (NextJS or Unity).
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

from .config import load_project_config, ensure_project_root

def generate_nextjs_feature_template(config, feature_name: str, issue_id: str = None) -> str:
    """Generate a feature template for NextJS projects."""
    
    title = feature_name.replace('-', ' ').replace('_', ' ').title()
    
    template = f"""# {title} Feature

## Overview

Implementation of {title.lower()} feature for the {config.name} NextJS application.

**Issue**: {f'#{issue_id}' if issue_id else 'TBD'}  
**Created**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Tasks

### Frontend Components
- [ ] Create {title} component in `{config.get_component_path(feature_name)}`
- [ ] Add component styling (Tailwind CSS)
- [ ] Implement responsive design
- [ ] Add loading and error states

### API Integration
"""
    
    if config.data_fetching == "trpc":
        template += f"""- [ ] Create tRPC router for {feature_name} in `{config.src_dir}/app/api/trpc/[trpc]/route.ts`
- [ ] Add {feature_name} procedures (queries/mutations)
- [ ] Implement tRPC client calls in component
"""
    else:  # SWR
        template += f"""- [ ] Create API endpoint in `{config.get_api_path(feature_name)}`
- [ ] Implement SWR hooks for data fetching
- [ ] Add error handling and revalidation
"""
    
    template += f"""
### Database/State Management
- [ ] Define data models/types in `{config.src_dir}/types/{feature_name}.ts`
- [ ] Implement database schema (if needed)
- [ ] Add state management (if complex state)

### Testing
- [ ] Unit tests for component: `{config.get_test_path(feature_name)}`
- [ ] API endpoint tests: `{config.tests_dir}/api/{feature_name}.test.ts`
- [ ] E2E tests: `{config.tests_dir}/e2e/{feature_name}.spec.ts`
- [ ] Test edge cases and error scenarios

### Documentation
- [ ] Update component documentation
- [ ] Add API documentation
- [ ] Update README if needed

## Acceptance Criteria

- [ ] Component renders correctly across all screen sizes
- [ ] All user interactions work as expected
- [ ] Data loads and updates properly
- [ ] Error states are handled gracefully
- [ ] Loading states provide good UX
- [ ] All tests pass (unit, integration, E2E)
- [ ] Code follows project linting standards
- [ ] Component is accessible (WCAG guidelines)

## Files to Create/Modify

### New Files
- `{config.get_component_path(feature_name)}` - Main component
- `{config.src_dir}/types/{feature_name}.ts` - TypeScript definitions
- `{config.get_test_path(feature_name)}` - Component tests
- `{config.tests_dir}/api/{feature_name}.test.ts` - API tests
- `{config.tests_dir}/e2e/{feature_name}.spec.ts` - E2E tests
"""
    
    if config.data_fetching == "swr":
        template += f"- `{config.get_api_path(feature_name)}` - API endpoint\n"
    
    template += f"""
### Modified Files
- `{config.src_dir}/app/layout.tsx` or `{config.src_dir}/app/page.tsx` - Import new component
- Navigation components (if adding new routes)
- Type definitions (if extending existing types)

## Technical Notes

### Component Structure
```tsx
// Example component structure
export interface {title}Props {{
  // Props interface
}}

export default function {title}Component({{ }}: {title}Props) {{
  // Component implementation
}}
```

### API Integration
"""
    
    if config.data_fetching == "trpc":
        template += """```typescript
// tRPC usage example
const { data, isLoading, error } = api.featureName.getAll.useQuery();
const mutation = api.featureName.create.useMutation();
```"""
    else:
        template += """```typescript
// SWR usage example
const { data, error, isLoading } = useSWR('/api/feature-name', fetcher);
```"""
    
    template += f"""

### Testing Strategy
- **Unit Tests**: Component logic, utility functions
- **Integration Tests**: API endpoints, database operations  
- **E2E Tests**: Complete user workflows
- **Accessibility Tests**: Screen reader compatibility, keyboard navigation

## Definition of Done

- [ ] All tasks completed and checked off
- [ ] Code reviewed and approved
- [ ] All tests passing in CI/CD
- [ ] Feature deployed to staging
- [ ] QA testing completed
- [ ] Documentation updated
- [ ] Accessibility requirements met
- [ ] Performance benchmarks met

---

*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} for {config.name} ({config.type})*
"""
    
    return template

def generate_unity_feature_template(config, feature_name: str, issue_id: str = None) -> str:
    """Generate a feature template for Unity projects."""
    
    title = feature_name.replace('-', ' ').replace('_', ' ').title()
    class_name = feature_name.replace('-', '').replace('_', '').title()
    
    template = f"""# {title} Feature

## Overview

Implementation of {title.lower()} feature for the {config.name} Unity game.

**Issue**: {f'#{issue_id}' if issue_id else 'TBD'}  
**Created**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Tasks

### Core Scripts
- [ ] Create {class_name} script in `{config.get_component_path(class_name)}`
- [ ] Implement core functionality and game logic
- [ ] Add MonoBehaviour lifecycle methods
- [ ] Implement public fields for Unity Inspector

### Game Objects & Prefabs
- [ ] Create {title} GameObject in scene
- [ ] Design {title} prefab in `Assets/Prefabs/{class_name}.prefab`
- [ ] Configure component settings in Inspector
- [ ] Set up prefab variants if needed

### UI Integration
- [ ] Create UI elements in `{config.src_dir}/UI/{class_name}UI.cs`
- [ ] Design Canvas and UI layout
- [ ] Implement button interactions and events
- [ ] Add UI animations and transitions

### Game Mechanics
- [ ] Implement physics interactions (if applicable)
- [ ] Add collision detection and handling
- [ ] Integrate with existing game systems
- [ ] Add audio effects and visual feedback

### Testing
- [ ] Edit Mode tests: `{config.get_test_path(class_name)}`
- [ ] Play Mode tests: `{config.tests_dir}/PlayMode/{class_name}PlayTests.cs`
- [ ] Integration tests with other systems
- [ ] Performance testing and optimization

### Assets & Resources
- [ ] Add required sprites/textures to `Assets/Textures/`
- [ ] Create materials in `Assets/Materials/`
- [ ] Add audio clips to `Assets/Audio/`
- [ ] Configure prefab references

## Acceptance Criteria

- [ ] Feature works correctly in Play mode
- [ ] No console errors or warnings
- [ ] Performance is acceptable (60+ FPS)
- [ ] UI is responsive and intuitive
- [ ] Feature integrates well with existing systems
- [ ] All tests pass in Unity Test Runner
- [ ] Code follows Unity C# conventions
- [ ] Prefabs are properly configured
- [ ] Feature works on target platforms

## Files to Create/Modify

### New Files
- `{config.get_component_path(class_name)}` - Main feature script
- `{config.src_dir}/UI/{class_name}UI.cs` - UI controller
- `Assets/Prefabs/{class_name}.prefab` - Main prefab
- `{config.get_test_path(class_name)}` - Edit mode tests
- `{config.tests_dir}/PlayMode/{class_name}PlayTests.cs` - Play mode tests

### Asset Files
- `Assets/Textures/{class_name}/` - Texture assets
- `Assets/Materials/{class_name}.mat` - Materials
- `Assets/Audio/{class_name}/` - Audio clips

### Modified Files
- Scene files (adding GameObjects)
- Game Manager scripts (if integration needed)
- Player controller (if player interaction)
- UI Manager (if UI integration)

## Technical Notes

### Script Structure
```csharp
// Example MonoBehaviour structure
using UnityEngine;

public class {class_name} : MonoBehaviour
{{
    [Header("{title} Settings")]
    [SerializeField] private float someValue = 1.0f;
    
    private void Start()
    {{
        // Initialization
    }}
    
    private void Update()
    {{
        // Per-frame logic
    }}
}}
```

### Testing Strategy
- **Edit Mode Tests**: Logic validation, utility functions
- **Play Mode Tests**: GameObject behavior, scene interactions
- **Integration Tests**: System compatibility, performance
- **Manual Testing**: Player experience, edge cases

### Unity Integration
- Ensure proper layer assignments
- Configure physics materials and colliders
- Set up proper component dependencies
- Test in multiple scenes if applicable

## Definition of Done

- [ ] All tasks completed and checked off
- [ ] Code reviewed and approved
- [ ] All Unity tests passing
- [ ] No console errors in Play mode
- [ ] Performance profiled and optimized
- [ ] Feature tested on target platforms
- [ ] Prefabs properly configured
- [ ] Documentation updated
- [ ] Build testing completed

---

*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} for {config.name} ({config.type})*
"""
    
    return template

def main():
    """Main function to generate feature markdown."""
    parser = argparse.ArgumentParser(description="Generate feature markdown template")
    parser.add_argument("--feature", required=True, help="Feature name (e.g., user-auth, dashboard)")
    parser.add_argument("--issue", help="GitHub issue ID")
    parser.add_argument("--output", help="Output file path (default: docs/features/{feature}.md)")
    
    args = parser.parse_args()
    
    try:
        # Ensure we're in project root
        ensure_project_root()
        
        # Load project configuration
        config = load_project_config()
        
        print(f"🚀 Generating feature template for '{args.feature}'...")
        print(f"📋 Project: {config.name} ({config.type})")
        
        # Generate appropriate template
        if config.type == "nextjs":
            content = generate_nextjs_feature_template(config, args.feature, args.issue)
        elif config.type == "unity":
            content = generate_unity_feature_template(config, args.feature, args.issue)
        else:
            raise ValueError(f"Unsupported project type: {config.type}")
        
        # Determine output path
        if args.output:
            output_path = args.output
        else:
            output_path = f"{config.features_dir}/{args.feature}.md"
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Write the template
        with open(output_path, 'w') as f:
            f.write(content)
        
        print(f"✅ Feature template created: {output_path}")
        print(f"\n📋 Next steps:")
        print(f"1. Review and customize the template in your editor")
        print(f"2. Add specific requirements and acceptance criteria")
        print(f"3. Start implementing the tasks one by one")
        print(f"4. Check off completed tasks as you progress")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error generating feature template: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 