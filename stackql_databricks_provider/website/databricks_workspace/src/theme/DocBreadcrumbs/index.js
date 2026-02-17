import React from 'react';
import DocBreadcrumbs from '@theme-original/DocBreadcrumbs';
import StackqlDeployDropdown from '@site/src/components/StackqlDeployDropdown/StackqlDeployDropdown';

export default function DocBreadcrumbsWrapper(props) {
  return (
    <div className="breadcrumbs-with-actions">
      <DocBreadcrumbs {...props} />
      <StackqlDeployDropdown />
    </div>
  );
}
