import React, { useState } from 'react';
import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import styles from './SchemaTable.module.css';

function SchemaRow({ name, type, description, children, depth = 0 }) {
  const [expanded, setExpanded] = useState(false);
  const hasChildren = children && children.length > 0;

  return (
    <>
      <tr className={styles.row}>
        <td style={{ paddingLeft: `${depth * 24 + 12}px` }}>
          {hasChildren && (
            <span 
              className={styles.expander} 
              onClick={() => setExpanded(!expanded)}
            >
              {expanded ? '▼' : '▶'}
            </span>
          )}
          <CopyableCode code={name} />
        </td>
        <td><CopyableCode code={type} /></td>
        <td>{description}</td>
      </tr>
      {expanded && children?.map((child, idx) => (
        <SchemaRow key={idx} {...child} depth={depth + 1} />
      ))}
    </>
  );
}

export default function SchemaTable({ fields }) {
  return (
    <table className={styles.schemaTable}>
      <thead>
        <tr>
          <th>Name</th>
          <th>Datatype</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        {fields.map((field, idx) => (
          <SchemaRow key={idx} {...field} />
        ))}
      </tbody>
    </table>
  );
}