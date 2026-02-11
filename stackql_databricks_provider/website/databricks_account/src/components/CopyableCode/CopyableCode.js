import React, { useState } from 'react';
import Clipboard from 'clipboard';

const CopyableCode = ({ code }) => {
    const [isCopied, setIsCopied] = useState(false);

    const handleCopy = () => {
        const clipboard = new Clipboard('.copyable-code', {
            text: () => code,
        });

        clipboard.on('success', function() {
            setIsCopied(true);
            window.setTimeout(() => setIsCopied(false), 2000);
            clipboard.destroy();
        });
    };

    return (
        <span className="copyable-code-container">
            <code className="copyable-code" onClick={handleCopy}>
                {code}
            </code>
            {isCopied ? <span style={{ marginLeft: '10px', color: 'green' }}>Copied!</span> : null}
        </span>
    );
};

export default CopyableCode;
