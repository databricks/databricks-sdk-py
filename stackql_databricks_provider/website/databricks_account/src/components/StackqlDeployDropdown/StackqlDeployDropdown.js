import React, { useState } from 'react';
import Button from '@mui/material/Button';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import DownloadIcon from '@mui/icons-material/Download';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import {useLocation} from '@docusaurus/router';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './StackqlDeployDropdown.module.css';

function getResourceInfo(pathname, providerName) {
  // URL pattern: /services/{service}/{resource}
  const match = pathname.match(/\/services\/([^/]+)\/([^/]+)/);
  if (!match) return null;
  return {
    provider: providerName,
    service: match[1],
    resource: match[2],
  };
}

function generateTemplate(info) {
  if (!info) return '';
  const fqn = `${info.provider}.${info.service}.${info.resource}`;
  return `/*+ createorupdate */
INSERT INTO ${fqn} (
  -- add columns here
)
SELECT
  -- add values here
;

/*+ statecheck, retries=5, retry_delay=10 */
SELECT *
FROM ${fqn}
WHERE 1=1
-- add filters here
;

/*+ exports */
SELECT *
FROM ${fqn}
WHERE 1=1
-- add filters here
;

/*+ delete */
DELETE FROM ${fqn}
WHERE 1=1
-- add filters here
;
`;
}

export default function StackqlDeployDropdown() {
  const [anchorEl, setAnchorEl] = useState(null);
  const [copied, setCopied] = useState(false);
  const open = Boolean(anchorEl);
  const location = useLocation();
  const {siteConfig} = useDocusaurusContext();

  // Extract provider name from config title, e.g. "databricks_workspace"
  const providerName = siteConfig.customFields?.providerName
    || siteConfig.title?.match(/StackQL\s+(.+?)\s+Provider/)?.[1]?.toLowerCase()?.replace(/\s+/g, '_')
    || '';

  const info = getResourceInfo(location.pathname, providerName);

  // Only show on resource pages
  if (!info) return null;

  const template = generateTemplate(info);
  const filename = `${info.resource}.iql`;

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleDownload = () => {
    const blob = new Blob([template], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    handleClose();
  };

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(template);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      // Fallback for older browsers
      const textarea = document.createElement('textarea');
      textarea.value = template;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      document.body.removeChild(textarea);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
    handleClose();
  };

  return (
    <div className={styles.dropdownWrapper}>
      <Button
        variant="outlined"
        size="small"
        endIcon={<KeyboardArrowDownIcon />}
        onClick={handleClick}
        sx={{
          textTransform: 'none',
          fontFamily: 'var(--ifm-font-family-base)',
          fontWeight: 600,
          fontSize: '0.75rem',
          borderColor: 'var(--ifm-color-primary)',
          color: 'var(--ifm-color-primary)',
          '&:hover': {
            borderColor: 'var(--ifm-color-primary)',
            backgroundColor: 'rgba(0, 65, 101, 0.04)',
          },
        }}
      >
        stackql-deploy Template
      </Button>
      <Menu
        anchorEl={anchorEl}
        open={open}
        onClose={handleClose}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
        transformOrigin={{ vertical: 'top', horizontal: 'right' }}
        sx={{
          '& .MuiPaper-root': {
            fontFamily: 'var(--ifm-font-family-base)',
            minWidth: 180,
          },
        }}
      >
        <MenuItem onClick={handleDownload}>
          <ListItemIcon>
            <DownloadIcon fontSize="small" />
          </ListItemIcon>
          <ListItemText
            primaryTypographyProps={{
              fontSize: '0.85rem',
              fontFamily: 'var(--ifm-font-family-base)',
            }}
          >
            Download
          </ListItemText>
        </MenuItem>
        <MenuItem onClick={handleCopy}>
          <ListItemIcon>
            <ContentCopyIcon fontSize="small" />
          </ListItemIcon>
          <ListItemText
            primaryTypographyProps={{
              fontSize: '0.85rem',
              fontFamily: 'var(--ifm-font-family-base)',
            }}
          >
            {copied ? 'Copied!' : 'Copy'}
          </ListItemText>
        </MenuItem>
      </Menu>
    </div>
  );
}
